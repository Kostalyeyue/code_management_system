from flask import Flask
from .views.index import index
from .views.count import count


def create_app():

    app = Flask(__name__)
    app.config.from_object('settings.Config')


    app.register_blueprint(count)
    app.register_blueprint(index)
    return app