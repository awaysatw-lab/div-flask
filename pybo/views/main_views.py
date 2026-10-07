from flask import Blueprint, render_template, request, redirect, url_for, g, session
from pybo import db
from pybo.models import Review, TimeDeal, Notice
from datetime import datetime

bp = Blueprint('main', __name__, url_prefix='/')


# ==========================================
# 메인 페이지 및 타임딜 목록
# ==========================================

@bp.route('/')
def index():
    context = get_common_context()
    return render_template('index.html', **context)


@bp.route('/notice/')
def notice():
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='').strip()
    category = request.args.get('category', type=str, default='all').strip()

    notice_query = Notice.query.order_by(Notice.created_at.desc())
    if category and category != 'all':
        notice_query = notice_query.filter(Notice.category == category)
    if kw:
        search = f"%{kw}%"
        notice_query = notice_query.filter(Notice.subject.ilike(search) | Notice.content.ilike(search))

    notice_list = notice_query.paginate(page=page, per_page=10)
    category_list = ['전체', '시스템', '공모전', '투어안내', '이벤트', '안내']

    return render_template('notice.html',
                           notice_list=notice_list,
                           page=page,
                           kw=kw,
                           category=category,
                           category_list=category_list)


@bp.route('/notice/<int:notice_id>/')
def notice_detail(notice_id):
    notice_obj = Notice.query.get_or_404(notice_id)
    notice_obj.views = (notice_obj.views or 0) + 1
    db.session.commit()

    # 해당 공지사항이 위치한 페이지 자동 계산 (10개씩 페이징 기준)
    newer_count = Notice.query.filter(Notice.created_at > notice_obj.created_at).count()
    page = (newer_count // 10) + 1
    notice_list = Notice.query.order_by(Notice.created_at.desc()).paginate(page=page, per_page=10)
    category_list = ['전체', '시스템', '공모전', '투어안내', '이벤트', '안내']

    return render_template('notice.html',
                           selected_notice_id=notice_id,
                           notice_list=notice_list,
                           page=page,
                           kw='',
                           category='all',
                           category_list=category_list)


# ==========================================
# 슬라이드 상품
# ==========================================
@bp.route('/main')
def main():
    context = get_common_context()
    return render_template('index.html', **context)


@bp.route('/autumn-detail')
def autumn_detail():
    context = get_common_context()
    return render_template('index.html', **context)


# ==========================================
# 지역 아이콘 상품
# ==========================================
@bp.route('/region/seoul')
def region_seoul():
    return redirect(url_for('product.main_product', region='sudo'))


@bp.route('/region/gangwon')
def region_gangwon():
    return redirect(url_for('product.main_product', region='gang'))


@bp.route('/region/chungcheong')
def region_chungcheong():
    return redirect(url_for('product.main_product', region='chung'))


@bp.route('/region/gyeongsang')
def region_gyeongsang():
    return redirect(url_for('product.main_product', region='geong'))


@bp.route('/region/jeolla')
def region_jeolla():
    return redirect(url_for('product.main_product', region='jeon'))


@bp.route('/region/jeju')
def region_jeju():
    return redirect(url_for('product.main_product', region='jeju'))


# ==========================================
# 리뷰 조회 및 상세
# ==========================================
@bp.route('/reviews/')
def review_list():
    return redirect(url_for('review.list'))


@bp.route('/review/detail/<int:review_id>/')
def review_detail(review_id):
    review = Review.query.get_or_404(review_id)
    return redirect(url_for('review.detail', product_id=review.product_id, review_id=review.id))


@bp.route('/deal/detail/<int:deal_id>/')
def deal_detail(deal_id):
    TimeDeal.query.get_or_404(deal_id)
    return redirect(url_for('product.main_product'))


# 언어 변경
@bp.route('/set-language/<lang_code>')
def set_language(lang_code):
    session['lang'] = lang_code
    return redirect(request.referrer or url_for('main.index'))


# ==========================================
# 공통 데이터 처리 컨텍스트 (메인 1개, 서브 2개 제한 적용)
# ==========================================

def get_common_context():
    review_list = Review.query.order_by(Review.created_at.desc()).all()
    main_deal = TimeDeal.query.filter_by(product_type='main').first()
    sub_deal_list = TimeDeal.query.filter_by(product_type='sub').limit(2).all()

    latest_notices = Notice.query.order_by(Notice.created_at.desc()).limit(3).all()

    print(f"==================================================")
    print(f"=== 현재 DB에서 가져온 전체 여행 후기 개수: {len(review_list)}개 ===")
    if len(review_list) > 0:
        review_title = review_list[0].title if hasattr(review_list[0], 'title') else (
            review_list[0].subject if hasattr(review_list[0], 'subject') else review_list[0].content[:10])
        print(f"=== 첫 번째 후기 내용: {review_title}")
    print(f"=== 메인 타임딜 타겟: {main_deal.title if main_deal else '없음'}")
    print(f"=== 서브 타임딜 노출 개수: {len(sub_deal_list)}개 ===")
    print(f"=== 최신 공지사항 개수: {len(latest_notices)}개 ===")
    print(f"==================================================")

    return {
        'review_list': review_list,
        'main_deal': main_deal,
        'sub_deal_list': sub_deal_list,
        'latest_notices': latest_notices,
        'now': datetime.now()
    }