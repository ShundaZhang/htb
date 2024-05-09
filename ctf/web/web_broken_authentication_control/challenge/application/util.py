from flask import session, request, abort, g
import string, functools, random, re 
from application.models import todo

generate = lambda x: ''.join([random.choice(string.hexdigits) for _ in range(x)])

def verify_integrity(func):
	def check_secret(secret, name):
		if secret != todo.get_secret_from(name):
			return abort(403)

	@functools.wraps(func)
	def check_integrity(*args, **kwargs):
		g.secret = request.args.get('secret', '') or request.form.get('secret', '')

		if request.view_args:
			list_access = request.view_args.get('assignee', '')

			if list_access and list_access != g.user:
				return abort(403)

			todo_id = request.view_args.get('todo_id', '')
			if todo_id:
				g.selected = todo.get_by_id(todo_id)

				if g.selected: 
					if dict(g.selected).get('assignee') == g.user:
						check_secret(g.secret, g.user)
						return func(*args, **kwargs)
					
					return abort(403)

				return abort(404)

		if request.is_json:
			g.task = request.get_json()
			g.name = g.task.get('name', '')

			if g.name and len(g.name) <= 100 and not re.search('script|meta|link|src|on[a-z]', g.name, re.IGNORECASE):
				g.name = g.name.replace('<', '&lt;').replace('>', '&gt;')
				check_secret(g.task.get('secret', ''), g.user)
				return func(*args, **kwargs)

			return abort(400)
		
		check_secret(g.secret, g.user)

		return func(*args, **kwargs)
	return check_integrity