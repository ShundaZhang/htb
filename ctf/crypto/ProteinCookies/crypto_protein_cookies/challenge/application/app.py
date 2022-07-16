from flask import Flask
from .blueprints.routes import web, api

app = Flask(__name__)
app.config.from_object('application.config.Config')
app.url_map.strict_slashes = False

app.register_blueprint(web, url_prefix='/')
app.register_blueprint(api, url_prefix='/api')

@app.errorhandler(Exception)
def handle_error(error):
    message = error.description if hasattr(error, 'description') else [str(x) for x in error.args]
    response = {
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }

    return response, error.code if hasattr(error, 'code') else 500