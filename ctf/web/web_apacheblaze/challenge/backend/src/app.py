from flask import Flask, request, jsonify

app = Flask(__name__)

app.config['GAMES'] = {'magic_click', 'click_mania', 'hyper_clicker', 'click_topia'}
app.config['FLAG'] = 'HTB{f4k3_fl4g_f0r_t3st1ng}'

@app.route('/', methods=['GET'])
def index():
    game = request.args.get('game')

    if not game:
        return jsonify({
            'error': 'Empty game name is not supported!.'
        }), 400

    elif game not in app.config['GAMES']:
        return jsonify({
            'error': 'Invalid game name!'
        }), 400

    elif game == 'click_topia':
        if request.headers.get('X-Forwarded-Host') == 'dev.apacheblaze.local':
            return jsonify({
                'message': f'{app.config["FLAG"]}'
            }), 200
        else:
            return jsonify({
                'message': 'This game is currently available only from dev.apacheblaze.local.'
            }), 200

    else:
        return jsonify({
            'message': 'This game is currently unavailable due to internal maintenance.'
        }), 200
