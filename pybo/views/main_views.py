from flask import Blueprint, render_template, request, redirect, url_for, g, session
from pybo.models import Review, TimeDeal
from datetime import datetime

bp = Blueprint('main', __name__, url_prefix='/')


def get_common_context():
    review_list = Review.query.order_by(Review.created_at.desc()).all()
    all_deals = TimeDeal.query.all()
    print(f"=== 현재 DB에서 가져온 타임딜 개수: {len(all_deals)}개 ===")

    main_deal = all_deals[0] if len(all_deals) > 0 else None
    sub_deal_list = all_deals[1:] if len(all_deals) > 1 else []

    return {
        'review_list': review_list,
        'main_deal': main_deal,
        'sub_deal_list': sub_deal_list,
        'now': datetime.now()
    }

# ==========================================
# 메인 페이지 및 타임딜 목록
# ==========================================
@bp.route('/')
def index():
    context = get_common_context()
    return render_template('index.html', **context)

@bp.route('/notice/')
def notice():
    # templates/main_fragments/main_notice.html 파일을 렌더링
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
# 테마 아이콘 상품
# ==========================================
@bp.route('/theme/resort')
def theme_resort():
    context = get_common_context()
    return render_template('index.html', **context)


@bp.route('/theme/experience')
def theme_experience():
    context = get_common_context()
    return render_template('index.html', **context)


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


@bp.route('/deal/detail/<int:deal_id>/')
def deal_detail(deal_id):
    deal = TimeDeal.query.get_or_404(deal_id)

    return render_template('product/deal_detail.html', deal=deal)

# 언어 변경
@bp.route('/set-language/<lang_code>')
def set_language(lang_code):
    session['lang'] = lang_code

    return redirect(request.referrer or url_for('main.index'))


def get_common_context():
    review_list = Review.query.order_by(Review.created_at.desc()).all()
    all_deals = TimeDeal.query.all()

    # === [디버깅 코드 추가] 콘솔창에서 후기 데이터를 확인합니다 ===
    print(f"==================================================")
    print(f"=== 현재 DB에서 가져온 전체 여행 후기 개수: {len(review_list)}개 ===")
    if len(review_list) > 0:
        print(
            f"=== 첫 번째 후기 제목/내용: {review_list[0].subject if hasattr(review_list[0], 'subject') else review_list[0].content[:10]}")
    print(f"==================================================")

    main_deal = all_deals[0] if len(all_deals) > 0 else None
    sub_deal_list = all_deals[1:] if len(all_deals) > 1 else []

    return {
        'review_list': review_list,
        'main_deal': main_deal,
        'sub_deal_list': sub_deal_list,
        'now': datetime.now()
    }