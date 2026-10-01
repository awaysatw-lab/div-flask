from flask import Blueprint, render_template, request, redirect, url_for, g
from pybo.models import Review, TimeDeal
from datetime import datetime

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    # 데이터베이스에서 필요한 모든 데이터를 한 번에 가져옵니다.
    review_list = Review.query.order_by(Review.created_at.desc()).all()
    main_deal = TimeDeal.query.filter_by(product_type='main').first()
    sub_deals = TimeDeal.query.filter_by(product_type='sub').limit(2).all()

    # 렌더링할 메인 템플릿 파일이 index.html인지 travel_package.html인지 프로젝트에 맞게 지정하세요.
    # 여기서는 기존 메인 템플릿 이름인 'index.html'로 통합 전달합니다.
    return render_template('index.html',
                           review_list=review_list,
                           main_deal=main_deal,
                           sub_deals=sub_deals,
                           now=datetime.now())


# ==========================================
# 슬라이드 상품
# ==========================================
@bp.route('/main')
def main():
    return render_template('index.html')


@bp.route('/autumn-detail')
def autumn_detail():
    return render_template('index.html')


# ==========================================
# 지역 아이콘 상품
# ==========================================
@bp.route('/region/seoul')
def region_seoul():
    return render_template('index.html')


@bp.route('/region/gangwon')
def region_gangwon():
    return render_template('index.html')


@bp.route('/region/chungcheong')
def region_chungcheong():
    return render_template('index.html')


@bp.route('/region/gyeongsang')
def region_gyeongsang():
    return render_template('index.html')


@bp.route('/region/jeolla')
def region_jeolla():
    return render_template('index.html')


@bp.route('/region/jeju')
def region_jeju():
    return render_template('index.html')


# ==========================================
# 테마 아이콘 상품
# ==========================================
@bp.route('/theme/resort')
def theme_resort():
    return render_template('index.html')


@bp.route('/theme/experience')
def theme_experience():
    return render_template('index.html')


# ==========================================
# 리뷰 조회 및 상세
# ==========================================
@bp.route('/reviews/')
def review_list():
    review_list = Review.query.order_by(Review.created_at.desc()).all()
    return render_template('review/review_list.html', review_list=review_list)


@bp.route('/review/detail/<int:review_id>/')
def review_detail(review_id):
    review = Review.query.get_or_404(review_id)
    return render_template('review/review_detail.html', review=review)


# ==========================================
# ⭕ 2. 타임딜 상품 상세 페이지 (중복 제거 후 동적 매핑만 유지)
# ==========================================
@bp.route('/deal/detail/<int:deal_id>/')
def deal_detail(deal_id):
    deal = TimeDeal.query.get_or_404(deal_id)
    return render_template('deal/deal_detail.html', deal=deal)