from flask import Flask, render_template


def create_app():
    app  = Flask(__name__)

    @app.route('/')
    def index():
        return "flask team project!!"

    @app.route('/chs')
    def chs():
        return render_template('chs.html')

    return app