import ast
from flask import render_template, Blueprint, request
from pybo.models import TourProduct, Review

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

    return render_template('product/sub_product.html',
                           product=selected_product, reviews=product_review,
                           product_images=product_images,
                           product_itinerary=product_itinerary,
                           product_details=product_details)



