import ast
from flask import render_template, Blueprint, request, session, g, jsonify
from pybo.models import TourProduct, Review
from sqlalchemy import text


bp = Blueprint('product', __name__, url_prefix='/product')

REGION_ALIAS = {
    'all': 'all',
    'sudo': 'sudo',
    'seoul': 'sudo',
    'gang': 'gang',
    'gangwon': 'gang',
    'chung': 'chung',
    'chungcheong': 'chung',
    'geong': 'geong',
    'gyeongsang': 'geong',
    'jeon': 'jeon',
    'jeolla': 'jeon',
    'jeju': 'jeju'
}

@bp.route('/main_product')
def main_product():
    kw = request.args.get('kw', default='', type=str).strip()
    raw_region = request.args.get('region', 'all').lower()
    selected_region = REGION_ALIAS.get(raw_region, 'all')

    query = TourProduct.query
    if kw:
        query = query.filter(TourProduct.name.ilike(f"%{kw}%"))

    products_data = query.all()

    return render_template(
        'product/main_product.html',
        products=products_data,
        selected_region=selected_region,
        kw=kw
    )


@bp.route('/sub_product/<int:product_id>')
def sub_product(product_id):
    selected_product = TourProduct.query.get_or_404(product_id)
    product_review = Review.query.filter_by(product_id=product_id).all()
    product_images = selected_product.get_image_list()

    # itinerary
    raw_itinerary = selected_product.itinerary_json
    product_itinerary = []

    if isinstance(raw_itinerary, str) and raw_itinerary.strip():
        try:
            product_itinerary = ast.literal_eval(raw_itinerary)
        except Exception:
            product_itinerary = []
    elif isinstance(raw_itinerary, list):
        product_itinerary = raw_itinerary

    # details
    raw_details = selected_product.detail_content
    product_details = {}

    if isinstance(raw_details, str) and raw_details.strip():
        try:
            product_details = ast.literal_eval(raw_details)
        except Exception:
            product_details = {}
    elif isinstance(raw_details, dict):
        product_details = raw_details

    session_db = TourProduct.query.session
    is_liked = False
    if g.user:
        check_query = text("SELECT user_id FROM direct_product_like WHERE user_id = :u_id AND product_id = :p_id")
        already_liked = session_db.execute(check_query, {'u_id': g.user.id, 'p_id': product_id}).fetchone()
        if already_liked:
            is_liked = True  # 추천한 기록이 있다면 True로 변경

    return render_template('product/sub_product.html',
                           product=selected_product, reviews=product_review,
                           product_images=product_images,
                           product_itinerary=product_itinerary,
                           product_details=product_details,
                           is_liked=is_liked)


@bp.route('/sub_product/like', methods=['POST'])
def toggle_product_like():
    # 2. 자바스크립트가 보낸 JSON 데이터 파싱
    data = request.get_json() or {}
    product_id = data.get('product_id')

    if not product_id:
        return jsonify({'error': 'bad_request'}), 400

    selected_product = TourProduct.query.get_or_404(product_id)
    session_db = selected_product.query.session

    create_table_query = """
                         CREATE TABLE IF NOT EXISTS direct_product_like
                         (user_id INTEGER NOT NULL, 
                            product_id INTEGER NOT NULL,
                             PRIMARY KEY(user_id, product_id)
                             ); 
                         """
    try:
        session_db.execute(text(create_table_query))
        session_db.commit()  # 테이블 생성을 먼저 확실하게 커밋
    except Exception:
        session_db.rollback()  # 이미 테이블이 존재하는 등의 이유로 에러가 나면 롤백 후 진행

    # 3. DB에서 현재 유저가 이 상품을 이미 추천했는지 조회
    check_query = text("SELECT user_id FROM direct_product_like WHERE user_id = :u_id AND product_id = :p_id")
    already_liked = session_db.execute(check_query, {'u_id': g.user.id, 'p_id': product_id}).fetchone()

    if already_liked:
        # 4-A. 이미 추천 이력이 DB에 있다면 -> 추천 취소 처리
        selected_product.recommendation_count = max(0, selected_product.recommendation_count - 1)

        # DB에서 추천 기록 삭제
        delete_query = text("DELETE FROM direct_product_like WHERE user_id = :u_id AND product_id = :p_id")
        session_db.execute(delete_query, {'u_id': g.user.id, 'p_id': product_id})
        status = "canceled"
    else:
        # 4-B. 추천한 적이 없다면 -> 추천 처리
        selected_product.recommendation_count += 1

        # DB에 새로운 추천 기록 추가
        insert_query = text("INSERT INTO direct_product_like (user_id, product_id) VALUES (:u_id, :p_id)")
        session_db.execute(insert_query, {'u_id': g.user.id, 'p_id': product_id})
        status = "liked"

    # 5. 숫자 카운트와 추천 기록을 DB에 최종 커밋
    try:
        session_db.commit()
    except Exception as e:
        session_db.rollback()
        return jsonify({'error': 'database_error', 'details': str(e)}), 500

    return jsonify({
        'success': True,
        'status': status,
        'recommendation_count': selected_product.recommendation_count
    }), 200

