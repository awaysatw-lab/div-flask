from flask import Flask, render_template


def create_app():
    app  = Flask(__name__)

    @app.route('/')
    def index():
        return "flask team project!!"

    @app.route('/hj')
    def hj():
        return render_template('hj.html')
    return app