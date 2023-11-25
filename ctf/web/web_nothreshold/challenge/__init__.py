from app.blueprints.verify2fa import *
from app.blueprints.dashboard import *
from app.blueprints.login import *
from app.blueprints.index import *
from app.config import Config
from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = Config.SECRET_KEY

app.register_blueprint(index_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(login_bp, url_prefix="/auth")
app.register_blueprint(verify2fa_bp, url_prefix="/auth")
