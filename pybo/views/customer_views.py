from flask import Blueprint, render_template, redirect, url_for, g, flash, request
from pybo import db
from pybo.models import Question
from pybo.forms import QuestionForm

bp = Blueprint('customer', __name__, url_prefix='/customer')


@bp.route('/faq')
def faq_list():
    if g.user is None:
        flash('로그인이 필요한 서비스입니다.')
        return redirect(url_for('auth.login', next=request.full_path))

    question_list = Question.query.filter_by(email=g.user.email) \
        .order_by(Question.create_date.desc()).all()
    return render_template('customer/faq.html', question_list=question_list)


@bp.route('/question/create/', methods=('GET', 'POST'))
def create():
    if g.user is None:
        flash('로그인이 필요한 서비스입니다.')
        return redirect(url_for('auth.login', next=request.full_path))

    form = QuestionForm()
    if form.validate_on_submit():
        question = Question(
            subject=form.subject.data,
            email=form.email.data,
            content=form.content.data
        )
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('customer.faq_list'))

    if g.user and not form.email.data:
        form.email.data = g.user.email

    return render_template('customer/question_form.html', form=form)
