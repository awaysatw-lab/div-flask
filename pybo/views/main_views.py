from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        print("아이디:", username)
        print("비밀번호:", password)

        return redirect(url_for('main.index'))

    return render_template('auth/login.html')

@bp.route('/signup/')
def signup():
    return render_template('auth/signup.html')