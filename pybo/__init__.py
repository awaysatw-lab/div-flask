
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate

import config

naming_convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(column_0_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s',
}

db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    from . import models

    from pybo.views.auth_views import oauth as auth_oauth
    auth_oauth.init_app(app)

    from .views import auth_views
    app.register_blueprint(auth_views.bp)

    from .views import order_views
    app.register_blueprint(order_views.bp)

    from .views import main_views
    app.register_blueprint(main_views.bp)

    from .views import review_views
    app.register_blueprint(review_views.bp)

    from .views import product_views
    app.register_blueprint(product_views.bp)

    from .views import customer_views
    app.register_blueprint(customer_views.bp)

    from .timedealseed import seed_time_deals
    with app.app_context():
        seed_time_deals()

    return app