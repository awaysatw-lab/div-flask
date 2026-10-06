from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import func

from pybo import db
from pybo.models import TourProduct, Review, User

bp = Blueprint('review', __name__, url_prefix='/review')

@bp.route('/list')
def list():
    page = request.args.get('page', default=1, type=int)
    region = request.args.get('region', default='', type=str).strip()
    kw = request.args.get('kw', default='', type=str).strip()

    # 상단 이달의 베스트 후기용 (리뷰 수가 많은 인기 상품 상위 3개)
    popular_products = db.session.query(TourProduct, func.count(Review.id).label('review_count')) \
        .outerjoin(TourProduct.reviews) \
        .group_by(TourProduct.id) \
        .order_by(func.count(Review.id).desc()) \
        .all()

    # 전체 후기 목록 쿼리 (상품 및 작성자 조인)
    review_query = Review.query.join(TourProduct).outerjoin(User)

    if region and region not in ('전체', '전체선택', '전체보기'):
        review_query = review_query.filter(TourProduct.region == region)

    if kw:
        search_kw = f"%{kw}%"
        review_query = review_query.filter(
            Review.title.ilike(search_kw) |
            Review.content.ilike(search_kw) |
            TourProduct.name.ilike(search_kw) |
            TourProduct.region.ilike(search_kw) |
            User.name.ilike(search_kw) |
            User.user_id.ilike(search_kw)
        )

    review_list = review_query.order_by(Review.created_at.desc()).paginate(page=page, per_page=10)

    # DB에 존재하는 고유 권역 목록
    distinct_regions = [r[0] for r in db.session.query(TourProduct.region).distinct().order_by(TourProduct.region).all()]

    return render_template(
        'review/review_list.html',
        popular_products=popular_products,
        review_list=review_list,
        region_list=distinct_regions,
        selected_region=region,
        kw=kw
    )

@bp.route('/detail/<int:product_id>')
def detail(product_id):
    selected_product = TourProduct.query.get_or_404(product_id)
    all_product_reviews = db.session.query(Review).filter_by(product_id=product_id).order_by(Review.created_at.desc()).all()
    review_count = len(all_product_reviews)
    latest_review_date = all_product_reviews[0].created_at.strftime('%Y-%m-%d') if all_product_reviews else None
    avg_rating = round(sum(r.rating for r in all_product_reviews) / review_count, 1) if review_count > 0 else 0.0

    review_id = request.args.get('review_id', type=int)
    selected_review = None

    if review_id:
        target_review = Review.query.filter_by(id=review_id, product_id=product_id).first()
        if target_review:
            reviews = [target_review]
            selected_review = target_review
        else:
            reviews = all_product_reviews
    else:
        reviews = all_product_reviews

    return render_template(
        "review/review_detail.html",
        product=selected_product,
        reviews=reviews,
        selected_review=selected_review,
        review_count=review_count,
        latest_review_date=latest_review_date,
        avg_rating=avg_rating
    )

@bp.route('/view/<int:review_id>')
def view(review_id):
    review = Review.query.get_or_404(review_id)
    return redirect(url_for('review.detail', product_id=review.product_id, review_id=review.id))