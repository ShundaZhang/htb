from application.database import query_db

class todo(object):
	def __init__(self, id, name, assignee, done=int(0)):
		self.name = name
		self.id = id 
		self.assignee = assignee
		self.done = done

	def __str__(self):
		return f'({self.id}, {self.name}, {self.assignee}, {self.done})'
	
	def asdict(self):
		return {
			'name': self.name,
			'id': self.id,
			'assignee': self.assignee,
			'done': self.done
		}


	def __iter__(self):
		return iter(self.__dict__.items())

	@staticmethod
	def get_bot_password():
		return query_db('SELECT password FROM bot', one=True)['password']

	@staticmethod
	def check_bot(password):
		return query_db('SELECT * FROM bot WHERE password=?', (password,), one=True)

	@staticmethod
	def create_user(name, secret):
		return query_db('INSERT INTO users (name, secret) VALUES (?, ?)', (name, secret))
	
	@staticmethod
	def get_secret_from(name):
		from flask import session
		try: 
			return query_db('SELECT secret FROM users WHERE name=?', (name,), one=True)['secret']
		except: 
			session.clear()
			pass

	@staticmethod
	def verify_secret(name, secret):
		return query_db('SELECT secret FROM users WHERE name=?', (name), one=True) == secret

	@staticmethod
	def add(name, assignee):
		return query_db('INSERT INTO todos (name, assignee, done) VALUES (?, ?, ?)', (name, assignee, int(0)))

	def complete(self):
		self.done = not self.done
		return query_db('UPDATE todos SET done=? WHERE id=?', (int(self.done), self.id))

	def delete(self):
		return query_db('DELETE FROM todos WHERE id=?', (self.id,))

	def reassign(self, new_assignee):
		return query_db('UPDATE todos SET assignee=? WHERE id=?', (new_assignee, self.id))

	def rename(self, new_name):
		return query_db('UPDATE todos SET name=? WHERE id=?', (new_name, self.id))

	@classmethod
	def get_all(cls):
		cls.todo = []
		for task in query_db('SELECT * FROM todos'):
			cls.todo.append(todo(task['id'], task['name'], task['assignee'], bool(task['done'])))
		return cls.todo

	@classmethod
	def get_by_id(cls, todo_id):
		task = query_db('SELECT * FROM todos WHERE id=?', (todo_id,), one=True)
		if task is not None:
			return todo(task['id'], task['name'], task['assignee'], task['done'])
		return []

	@classmethod
	def get_by_user(cls, assignee):
		cls.todo = []
		for task in query_db('SELECT * FROM todos WHERE assignee=?', (assignee,)):
			cls.todo.append(todo(task['id'], task['name'], task['assignee'], bool(task['done'])))
		return cls.todo