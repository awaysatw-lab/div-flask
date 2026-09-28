from flask import Blueprint, render_template

bp = Blueprint('review', __name__, url_prefix='/review')

@bp.route('/list')
def review_list():
    return render_template('review_sam.html')