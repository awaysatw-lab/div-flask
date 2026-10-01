from flask import Blueprint, url_for, render_template, request, flash, redirect, session, g, jsonify
from werkzeug.security import check_password_hash, generate_password_hash


from pybo import db
from pybo.models import User
from pybo.forms import UserCreateForm, UserLoginForm

import re
import secrets
import string

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup/', methods=('GET', 'POST'))
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

        return render_template('auth/signup_success.html')

    if request.method == 'POST' and not form.validate():
        for field, errors in form.errors.items():
            for error in errors:
                flash(error)

    return render_template('auth/signup.html', form=form)


@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()

    if request.method == 'POST':
        user_id_input = request.form.get('user_id', '').strip()
        password_input = request.form.get('password', '').strip()

        if not user_id_input:
            flash("아이디를 입력해주세요.")
            return render_template('auth/login.html', form=form)

        if not password_input:
            flash("비밀번호를 입력해주세요.")
            return render_template('auth/login.html', form=form)

        if form.validate_on_submit():
            user = User.query.filter_by(user_id=form.user_id.data).first()

            if not user:
                flash("존재하지 않는 아이디입니다.")
                return render_template('auth/login.html', form=form)

            elif not check_password_hash(user.password_hash, form.password.data):
                flash("비밀번호가 올바르지 않습니다.")
                return render_template('auth/login.html', form=form)

            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))

        else:
            for field, errors in form.errors.items():
                for error in errors:
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

@bp.route('/find_id', methods=['POST'])
def find_id():
    try:
        data = request.get_json()
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()

        if not name or not email:
            return jsonify({'status': 'fail', 'message': '이름과 이메일을 모두 입력해주세요.'}), 400

        user = User.query.filter_by(name=name, email=email).first()

        if user:
            return jsonify({
                'status': 'success',
                'message': f'회원님의 아이디는 [{user.user_id}] 입니다.'
            })
        else:
            return jsonify({'status': 'fail', 'message': '일치하는 회원 정보가 존재하지 않습니다.'})

    except Exception as e:
        print(f"아이디 찾기 백엔드 에러: {str(e)}")
        return jsonify({'status': 'fail', 'message': '시스템 통신 에러가 발생했습니다.'}), 500


@bp.route('/find_pw', methods=['POST'])
def find_pw():
    try:
        data = request.get_json()
        user_id = data.get('user_id', '').strip()
        email = data.get('email', '').strip()

        if not user_id or not email:
            return jsonify({'status': 'fail', 'message': '아이디와 이메일을 모두 입력해주세요.'}), 400

        user = User.query.filter_by(user_id=user_id, email=email).first()

        if user:
            # 🌟 [들여쓰기 버그 수정 완료] 한 단계 안쪽으로 정교하게 마이그레이션했습니다.
            alphabet = string.ascii_letters + string.digits
            temp_password = ''.join(secrets.choice(alphabet) for _ in range(10))

            user.password_hash = generate_password_hash(temp_password)
            db.session.commit()

            print(f"🔥 [{user.user_id}]님의 실제 메일({user.email})로 임시비밀번호 [{temp_password}] 발송 완료 및 DB 적재 성공!")

            return jsonify({
                'status': 'success',
                'message': f'가입하신 이메일({user.email})로 임시 비밀번호를 발송했습니다.'
            })
        else:
            return jsonify({'status': 'fail', 'message': '아이디 또는 이메일 주소가 일치하지 않습니다.'})

    except Exception as e:
        db.session.rollback()
        print(f"비밀번호 찾기 백엔드 에러: {str(e)}")
        return jsonify({'status': 'fail', 'message': '시스템 통신 에러가 발생했습니다.'}), 500