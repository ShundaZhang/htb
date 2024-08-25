import os, json

import tornado.web

from application.util.general import generate, json_response, is_valid_url, is_request_from_localhost, update_tornados, read_file_contents, random_ip, random_hostname, random_status
from application.util.bot import bot_thread

class TornadoObject:
	def __init__(self, machine_id, ip_address, status):
		self.machine_id = machine_id
		self.ip_address = ip_address
		self.status = status

	def serialize(self):
		return vars(self)

class BaseHandler(tornado.web.RequestHandler):
	def set_default_headers(self):
		self.set_header("Access-Control-Allow-Origin", "*")
		self.set_header("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE,OPTIONS")
		self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization, x-requested-with")

	def write_error(self, status_code, **kwargs):
		self.set_header("Content-Type", "application/json")
		if "exc_info" in kwargs:
			exception = kwargs["exc_info"][1]
			message = exception.log_message if hasattr(exception, "log_message") else str(exception)
		else:
			message = self._reason
		
		self.finish(json_response(message, self.__class__.__name__, error=True))

class NotFoundHandler(BaseHandler):
	def prepare(self):
		self.set_status(404)
		self.write_error(404)

class IndexHandler(BaseHandler):
	def get(self):
		self.render("templates/index.html")

class GetTornadosHandler(BaseHandler):
	def initialize(self, tornados):
		self.tornados = tornados

	def get(self):
		self.set_header("Content-Type", "application/json")
		self.write(json.dumps([tornado.serialize() for tornado in self.tornados]))
			
class UpdateTornadoHandler(BaseHandler):
	def initialize(self, tornados):
		self.tornados = tornados

	def post(self):
		self.set_header("Content-Type", "application/json")
		if not is_request_from_localhost(self):
			self.set_status(403)
			self.write(json_response("Only localhost can update tornado status.", "Forbidden", error=True))
			return

		try:
			data = json.loads(self.request.body)
			machine_id = data.get("machine_id")

			for tornado in self.tornados:
				if tornado.machine_id == machine_id:
					update_tornados(data, tornado)
					self.write(json_response(f"Status updated for {machine_id}", "Update"))
					return

			self.set_status(404)
			self.write(json_response("Machine not found", "Not Found", error=True))
		except json.JSONDecodeError:
			self.set_status(400)
			self.write(json_response("Invalid JSON", "Bad Request", error=True))

class ReportTornadoHandler(BaseHandler):
	def initialize(self, tornados):
		self.tornados = tornados

	def get(self):
		self.set_header("Content-Type", "application/json")
		ip_param = self.get_argument("ip", None)
		tornado_url = f"http://{ip_param}/agent_details"
		if ip_param and is_valid_url(tornado_url):
			bot_thread(tornado_url)
			self.write(json_response(f"Tornado: {ip_param}, has been reported", "Reported"))
		else:
			self.set_status(400)
			self.write(json_response("IP parameter is required", "Bad Request", error=True))

class LoginHandler(BaseHandler):
	def post(self):
		self.set_header("Content-Type", "application/json")
		try:
			data = json.loads(self.request.body)
			username = data.get("username")
			password = data.get("password")

			for user in USERS:
				if user["username"] == username and user["password"] == password:
					self.set_secure_cookie("user", username)
					self.write(json_response("Login successful", "Login"))
				else:
					self.set_status(401)
					self.write(json_response("Invalid credentials", "Unauthorized", error=True))
				
				break

		except json.JSONDecodeError:
			self.set_status(400)
			self.write(json_response("Invalid JSON", "Bad Request", error=True))

class ProtectedContentHandler(BaseHandler):
	def get_current_user(self):
		return self.get_secure_cookie("user")

	def get(self):
		self.set_header("Content-Type", "application/json")
		if not self.current_user:
			self.set_status(401)
			self.write(json_response("Unauthorized access", "Unauthorized", error=True))
			return
		
		flag = read_file_contents("/flag.txt")
		self.write(json_response(flag, "Success"))

def make_app():
	settings = {
		"static_path": os.path.join(os.path.dirname(__file__), "static"),
		"cookie_secret": generate(32),
		"default_handler_class": NotFoundHandler,
		"autoreload": True
	}

	return tornado.web.Application([
		(r"/", IndexHandler),
		(r"/get_tornados", GetTornadosHandler, dict(tornados=TORNADOS)),
		(r"/update_tornado", UpdateTornadoHandler, dict(tornados=TORNADOS)),
		(r"/report_tornado", ReportTornadoHandler, dict(tornados=TORNADOS)),
		(r"/login", LoginHandler),
		(r"/stats", ProtectedContentHandler),
		(r".*", NotFoundHandler),
	], **settings)

TORNADOS = [
	TornadoObject(machine_id=random_hostname(), ip_address=random_ip(), status=random_status()),
    TornadoObject(machine_id=random_hostname(), ip_address=random_ip(), status=random_status()),
    TornadoObject(machine_id=random_hostname(), ip_address=random_ip(), status=random_status()),
    TornadoObject(machine_id=random_hostname(), ip_address=random_ip(), status=random_status()),
    TornadoObject(machine_id=random_hostname(), ip_address=random_ip(), status=random_status()),
    TornadoObject(machine_id=random_hostname(), ip_address=random_ip(), status=random_status()),
    TornadoObject(machine_id=random_hostname(), ip_address=random_ip(), status=random_status()),
    TornadoObject(machine_id=random_hostname(), ip_address=random_ip(), status=random_status()),
    TornadoObject(machine_id=random_hostname(), ip_address=random_ip(), status=random_status()),
    TornadoObject(machine_id=random_hostname(), ip_address=random_ip(), status=random_status()),
    TornadoObject(machine_id=random_hostname(), ip_address=random_ip(), status=random_status())
]

USERS = [
	{
		"username": "lean@tornado-service.htb",
		"password": generate(32),
	},
	{
		"username": "xclow3n@tornado-service.htb",
		"password": generate(32),
	},
	{
		"username": "makelaris@tornado-service.htb",
		"password": generate(32),
	}
]

APP = make_app()
