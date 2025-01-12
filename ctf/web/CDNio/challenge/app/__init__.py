from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    from .blueprints import main_bp, bot_bp, auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(bot_bp)
    app.register_blueprint(auth_bp)

    return app
