from flask import Blueprint, render_template, request, redirect, url_for, g, session
from pybo.models import Review, TimeDeal
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
    return render_template('/notice.html')


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

    return {
        'review_list': review_list,
        'main_deal': main_deal,
        'sub_deal_list': sub_deal_list,
        'now': datetime.now()
    }
