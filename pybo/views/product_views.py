from flask import render_template, Blueprint

from pybo import db
from pybo.models import User, TourProduct, RegionEnum


bp = Blueprint('product', __name__, url_prefix='/product')

@bp.route('/main_product')
def main_product():
    return render_template('product/main_product.html', products=products_data)

def seed_product():
    seed_database()



@bp.route('/sub_product')
def sub_product():
    return render_template('product/sub_product.html')


