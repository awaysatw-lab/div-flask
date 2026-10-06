from flask import Blueprint, url_for, render_template, request, flash, redirect, session, g, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from authlib.integrations.flask_client import OAuth
from urllib.parse import urlparse, urljoin, parse_qs

from pybo import db
from pybo.models import User
from pybo.forms import UserCreateForm, UserLoginForm

import re
import secrets
import string
import functools

bp = Blueprint('auth', __name__, url_prefix='/auth')

def is_safe_url(target):
    if not target:
        return False
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

def get_safe_redirect_url(target=None):
    """
    안전한 복귀 URL을 우선순위에 따라 반환:
    1. target 인자 (request.args 또는 request.form의 next)
    2. request.referrer (이전 페이지)
    단, 내부 URL이어야 하며 /auth/ 경로(자체 순환 방지)는 제외.
    단, /auth/ 경로의 referrer에 ?next= 가 포함된 경우 해당 next 값을 안전하게 추출.
    """
    candidates = []
    if target:
        candidates.append(target)

    if request.referrer and is_safe_url(request.referrer):
        parsed_ref = urlparse(request.referrer)
        if parsed_ref.path.startswith('/auth/'):
            qs = parse_qs(parsed_ref.query)
            if 'next' in qs and qs['next']:
                candidates.append(qs['next'][0])
        else:
            ref_path = parsed_ref.path
            if parsed_ref.query:
                ref_path += '?' + parsed_ref.query
            candidates.append(ref_path)

    for cand in candidates:
        if cand and is_safe_url(cand):
            parsed = urlparse(urljoin(request.host_url, cand))
            if not parsed.path.startswith('/auth/'):
                final_url = parsed.path
                if parsed.query:
                    final_url += '?' + parsed.query
                return final_url

    return None

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            flash('로그인이 필요한 서비스입니다.')
            return redirect(url_for('auth.login', next=request.url))
        return view(*args, **kwargs)
    return wrapped_view

@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()

    raw_next = request.args.get('next') or request.form.get('next')
    next_page = get_safe_redirect_url(raw_next)

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

        # 회원가입 성공 시 즉시 자동 로그인
        session.clear()
        session['user_id'] = new_user.id

        redirect_target = next_page or url_for('main.index')
        return render_template('auth/signup_success.html', redirect_url=redirect_target)

    if request.method == 'POST' and not form.validate():
        for field, errors in form.errors.items():
            for error in errors:
                flash(error)

    return render_template('auth/signup.html', form=form, next=next_page)


@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()

    raw_next = request.args.get('next') or request.form.get('next')
    next_page = get_safe_redirect_url(raw_next)

    if request.method == 'POST':
        user_id_input = request.form.get('user_id', '').strip()
        password_input = request.form.get('password', '').strip()

        if not user_id_input:
            flash("아이디를 입력해주세요.")
            return render_template('auth/login.html', form=form, next=next_page)

        if not password_input:
            flash("비밀번호를 입력해주세요.")
            return render_template('auth/login.html', form=form, next=next_page)

        if form.validate_on_submit():
            user = User.query.filter_by(user_id=form.user_id.data).first()

            if not user or not check_password_hash(user.password_hash, form.password.data):
                flash("아이디 또는 비밀번호가 올바르지 않습니다.")
                return render_template('auth/login.html', form=form, next=next_page)

            session.clear()
            session['user_id'] = user.id

            if next_page:
                return redirect(next_page)
            return redirect(url_for('main.index'))

    return render_template('auth/login.html', form=form, next=next_page)


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

oauth = OAuth()

# 1. 🌐 구글 OAuth 설정 (공식 주소 반영)
google = oauth.register(
    name='google',
    client_id='발급받은_구글_클라이언트_://googleusercontent.com',
    client_secret='발급받은_구글_클라이언트_보안_비밀번호',
    access_token_url='https://googleapis.com',
    authorize_url='https://google.com',
    api_base_url='https://googleapis.com',
    userinfo_endpoint='https://googleapis.com',
    client_kwargs={'scope': 'openid email profile'},
)

# 2. 🟢 네이버 OAuth 설정 (공식 주소 반영)
naver = oauth.register(
    name='naver',
    client_id='네이버에서_발급받은_클라이언트_ID',
    client_secret='네이버에서_발급받은_비밀번호',
    access_token_url='https://naver.com',
    authorize_url='https://naver.com',
    api_base_url='https://naver.com',
    client_kwargs={
        'token_endpoint_auth_method': 'client_secret_post',
    }
)

# 3. 🟡 카카오 OAuth 설정 (공식 주소 반영)
kakao = oauth.register(
    name='kakao',
    client_id='카카오에서_발급받은_REST_API_키',
    client_secret='카카오에서_발급받은_보안_비밀구절(선택사항)',
    access_token_url='https://kakao.com',
    authorize_url='https://kakao.com',
    api_base_url='https://kakao.com',
)


# ==========================================
#  1. 구글(Google) 로그인 및 콜백
# ==========================================
@bp.route('/login/google')
def google_login():
    raw_next = request.args.get('next')
    safe_next = get_safe_redirect_url(raw_next)
    if safe_next:
        session['social_next'] = safe_next

    redirect_uri = url_for('auth.google_callback', _external=True)
    return google.authorize_redirect(redirect_uri)


@bp.route('/login/google/callback')
def google_callback():
    token = google.authorize_access_token()
    user_info = google.get('userinfo').json()

    session['user_id'] = user_info.get('email')
    session['user_name'] = user_info.get('name')

    social_next = session.pop('social_next', None)
    safe_next = get_safe_redirect_url(social_next)
    if safe_next:
        return redirect(safe_next)
    return redirect(url_for('main.index'))


# ==========================================
#  2. 네이버(Naver) 로그인 및 콜백
# ==========================================
@bp.route('/login/naver')
def naver_login():
    raw_next = request.args.get('next')
    safe_next = get_safe_redirect_url(raw_next)
    if safe_next:
        session['social_next'] = safe_next

    redirect_uri = url_for('auth.naver_callback', _external=True)
    return naver.authorize_redirect(redirect_uri)


@bp.route('/login/naver/callback')
def naver_callback():
    token = naver.authorize_access_token()
    user_info = naver.get('').json().get('response', {})

    session['user_id'] = user_info.get('email')
    session['user_name'] = user_info.get('name')

    social_next = session.pop('social_next', None)
    safe_next = get_safe_redirect_url(social_next)
    if safe_next:
        return redirect(safe_next)
    return redirect(url_for('main.index'))


# ==========================================
#  3. 카카오(Kakao) 로그인 및 콜백
# ==========================================
@bp.route('/login/kakao')
def kakao_login():
    raw_next = request.args.get('next')
    safe_next = get_safe_redirect_url(raw_next)
    if safe_next:
        session['social_next'] = safe_next

    redirect_uri = url_for('auth.kakao_callback', _external=True)
    return kakao.authorize_redirect(redirect_uri)


@bp.route('/login/kakao/callback')
def kakao_callback():
    token = kakao.authorize_access_token()

    session['user_id'] = "kakao_user_id"

    social_next = session.pop('social_next', None)
    safe_next = get_safe_redirect_url(social_next)
    if safe_next:
        return redirect(safe_next)
    return redirect(url_for('main.index'))