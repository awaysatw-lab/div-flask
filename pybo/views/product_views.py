from flask import render_template, Blueprint
from pybo.models import TourProduct

from pybo import db
from pybo.models import User, TourProduct, Review


bp = Blueprint('product', __name__, url_prefix='/product')

@bp.route('/main_product')
def main_product():
    products_data = TourProduct.query.all()

    return render_template('product/main_product.html', products=products_data)

@bp.route('/sub_product/<int:product_id>')
def sub_product(product_id):
    selected_product = TourProduct.query.get_or_404(product_id)

    return render_template('product/sub_product.html', product=selected_product)


