
from flask import Blueprint, url_for, render_template, request, flash, redirect, session, g, jsonify
from werkzeug.security import check_password_hash


from pybo import db
from pybo.models import User
from pybo.forms import UserCreateForm, UserLoginForm

import re

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/signup', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()

    if request.method == 'POST' and form.validate_on_submit():
        new_user = User(
            user_id=form.user_id.data,
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data
        )

        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.index'))

    if request.method == 'POST' and not form.validate():
        for field, errors in form.errors.items():
            for error in errors:
                flash(error)

    return render_template('auth/signup.html', form=form)


@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(user_id=form.user_id.data).first()

        if not user:
            error = "존재하지 않는 아이디입니다."
        elif not check_password_hash(user.password_hash, form.password.data):
            error = "비밀번호가 올바르지 않습니다."

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))

        flash(error)

    return render_template('auth/login.html', form=form)


@bp.route('/check_id', methods=['POST'])
def check_id():
    data = request.get_json()
    user_id = data.get('user_id', '').strip()

    if not user_id:
        return jsonify({'status': 'fail', 'message': '아이디를 입력해 주세요.'}), 400

    if not re.match('^[a-zA-Z0-9]+$', user_id):
        return jsonify({'status': 'fail', 'message': '아이디는 영문 대소문자와 숫자만 사용 가능합니다.'}), 400

    if len(user_id) < 4 or len(user_id) > 25:
        return jsonify({'status': 'fail', 'message': '아이디는 4자 이상 25자 이하로 입력해 주세요.'}), 400

    user = User.query.filter_by(user_id=user_id).first()
    if user:
        return jsonify({'status': 'fail', 'message': '이미 사용 중인 아이디입니다.'})
    return jsonify({'status': 'success', 'message': '사용 가능한 아이디입니다.'})


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)
