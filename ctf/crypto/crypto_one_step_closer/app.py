from flask import *
from chall import encrypt_flag

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api/get_flag', methods=['GET'])
def get_flag():
    payload = encrypt_flag()
    return jsonify(payload)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
