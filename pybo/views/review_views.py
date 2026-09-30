from flask import Blueprint, render_template
from sqlalchemy import func

from pybo import db
from pybo.models import TourProduct, Review

bp = Blueprint('review', __name__, url_prefix='/review')

@bp.route('/list')
def list():
    # 리뷰가 많은 순으로 전체 상품 조회
    # 리뷰 개수 정보까지 한 번에 튜플로 가져오기
    popular_products = db.session.query(TourProduct, func.count(Review.id).label('review_count')) \
        .outerjoin(TourProduct.reviews) \
        .group_by(TourProduct.id) \
        .order_by(func.count(Review.id).desc()) \
        .all()
    # 최근 작성한 리뷰 순으로 전체 상품 조회
    # 리뷰 개수 정보까지 한 번에 튜플로 가져오기
    latest_products = db.session.query(
        TourProduct,
        func.count(Review.id).label('review_count'),
        func.max(Review.created_at).label('latest_review_date')  # 최근 리뷰일 추가
    ) \
    .outerjoin(TourProduct.reviews) \
    .group_by(TourProduct.id) \
    .order_by(func.max(Review.created_at).desc()) \
    .all()

    return render_template('review/review_list.html', popular_products=popular_products, latest_products=latest_products)

@bp.route('/detail/<int:product_id>')
def detail(product_id):
    return render_template("review/review_detail.html")