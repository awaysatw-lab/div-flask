import json

from flask import render_template, Blueprint, request

from pybo.forms import OrderReserveForm

from pybo import db
from pybo.models import User, TourProduct, Review, Order, Accommodation
from pybo.views.main_views import review_list

bp = Blueprint('product', __name__, url_prefix='/product')

@bp.route('/main_product')
def main_product():
    products_data = TourProduct.query.all()

    return render_template('product/main_product.html', products=products_data)


@bp.route('/sub_product/<int:product_id>')
def sub_product(product_id):
    selected_product = TourProduct.query.get_or_404(product_id)
    product_review = Review.query.filter_by(product_id=product_id).all()
    product_time = Order.query.all()
    house_list = Accommodation.query.all()

    if isinstance(selected_product.image_urls, str):
        try:
            valid_json_string = selected_product.image_urls.replace("'", '"')
            selected_product.image_urls = json.loads(valid_json_string)
        except Exception:
            selected_product.image_urls = selected_product.image_urls.strip("[]").replace("'", "").split(", ")

    return render_template('product/sub_product.html',
                           product=selected_product, reviews=product_review, times=product_time, houses=house_list)



@bp.route('/sub_product', methods=['GET'])
def reserve():
    headcount = request.args.get('headcount', 1, type=int)
    if headcount < 1:
        headcount = 1

    form = OrderReserveForm(headcount=headcount)

    return render_template('product/sub_product.html', headcount=headcount, form=form)

