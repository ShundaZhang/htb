from flask import Blueprint

bot_bp = Blueprint('bot_bp', __name__,)

from .routes import * 