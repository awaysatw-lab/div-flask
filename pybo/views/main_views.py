from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/main_product')
def main_product():
    return render_template('product/main_product.html')

@bp.route('/sub_product')
def sub_product():
    return render_template('product/sub_product.html')