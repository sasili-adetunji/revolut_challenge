from flask import Flask, Blueprint
from flask_restful import Api
from resources.nest import Nest


api_bp = Blueprint('api', __name__)
api = Api(api_bp)
api.add_resource(Nest, '')


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)