# pybo/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from pybo.models import User


# =========================================================================
# 1. 회원가입 검증 폼 (UserCreateForm)
# =========================================================================
class UserCreateForm(FlaskForm):
    user_id = StringField('아이디', validators=[
        DataRequired('아이디는 필수 입력 항목입니다.'),
        Length(min=4, max=25, message='아이디는 4자 이상 25자 이하로 입력해 주세요.'),
        Regexp('^[a-zA-Z0-9]+$', message='아이디는 영문 대소문자와 숫자만 사용할 수 있습니다.')
    ])

    name = StringField('이름', validators=[
        DataRequired('이름은 필수 입력 항목입니다.')
    ])

    email = EmailField('이메일', validators=[
        DataRequired('이메일은 필수 입력 항목입니다.'),
        Email('올바른 이메일 형식이 아닙니다.')
    ])

    phone = StringField('전화번호', validators=[
        DataRequired('전화번호는 필수 입력 항목입니다.')
    ])

    password = PasswordField('비밀번호', validators=[
        DataRequired('비밀번호는 필수 입력 항목입니다.'),
        Length(min=6, message='비밀번호는 최소 6자 이상이어야 합니다.')
    ])

    password_confirm = PasswordField('비밀번호 확인', validators=[
        DataRequired('비밀번호 확인은 필수 입력 항목입니다.'),
        EqualTo('password', message='비밀번호가 일치하지 않습니다.')
    ])

    def validate_user_id(self, field):
        if User.query.filter_by(user_id=field.data).first():
            raise ValidationError('이미 사용 중인 아이디입니다.')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('이미 등록된 이메일 주소입니다.')

    def validate_phone(self, field):
        if User.query.filter_by(phone=field.data).first():
            raise ValidationError('이미 등록된 전화번호입니다.')


class UserLoginForm(FlaskForm):
    user_id = StringField('아이디', validators=[
        DataRequired('아이디를 입력해 주세요.')
    ])
    password = PasswordField('비밀번호', validators=[
        DataRequired('비밀번호를 입력해 주세요.')
    ])
