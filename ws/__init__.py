from flask import Flask, Blueprint

latest = Blueprint('latest', __name__)


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config_name)

    # treat /some/url/ and /some/url the same
    app.url_map.strict_slashes = False

    from ws.interface import routes

    app.register_blueprint(latest)

    return app
