from flask import render_template, Blueprint
from pybo.models import TourProduct

bp = Blueprint('product', __name__, url_prefix='/product')

@bp.route('/main_product')
def main_product():
    products = TourProduct.query.order_by(TourProduct.id.asc()).all()
    return render_template('product/main_product.html', products=products)

@bp.route('/sub_product')
def sub_product():
    return render_template('product/sub_product.html')

