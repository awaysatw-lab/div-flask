from flask import render_template, Blueprint

bp = Blueprint('product', __name__, url_prefix='/product')

@bp.route('/main_product')
def main_product():
    return render_template('product/main_product.html')

@bp.route('/sub_product')
def sub_product():
    return render_template('product/sub_product.html')
