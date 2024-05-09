from flask import Flask, session, g
from flask.json import JSONEncoder
from application.blueprints.routes import main, api
from application.util import generate
from application.database import get_db
from application.models import todo
import time

class toJSON(JSONEncoder):
	def default(self, obj):
		if isinstance(obj, todo):
			return {
				'id' : obj.id,
				'name' : obj.name,
				'assignee': obj.assignee,
				'done' : obj.done
			}
		return super(toJSON, self).default(obj)

class HTB(Flask):
	def process_response(self, response):
		response.headers['Server'] = 'made with <3 by makelarides'
		super(HTB, self).process_response(response)
		return response

app = HTB(__name__)
app.config.from_object('application.config.Config')
app.json_encoder = toJSON

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(api, url_prefix='/api')

@app.before_first_request
def wake_bots():
	with app.open_resource('schema.sql', mode='r') as f:
		get_db().cursor().executescript(f.read() % (generate(15)))
	time.sleep(0.2)

@app.before_request
def is_authenticated():
	g.user = session.get('authentication')
	if not g.user:
		username = f'user{generate(8)}'
		todo.create_user(username, generate(15))
		g.user = session['authentication'] = username


@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None: db.close()

@app.errorhandler(404)
def not_found(error):
	return {'error': 'Not Found'}, 404

@app.errorhandler(403)
def forbidden(error):
	return {'error': 'Not Allowed'}, 403

@app.errorhandler(400)
def bad_request(error):
	return {'error': 'Bad Request'}, 400