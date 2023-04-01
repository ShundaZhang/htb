from flask import Flask

from routes import web, api

app = Flask(__name__)

app.register_blueprint(web, url_prefix='/')
app.register_blueprint(api, url_prefix='/api')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337)
