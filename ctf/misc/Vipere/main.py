import sys
import os
import subprocess
import socketserver
from datetime import datetime
from string import Formatter

class Station(socketserver.BaseRequestHandler):
	def get_loaded_commands(interface):
		secure_commands = SecureCommands([])
		return list(secure_commands.dispatcher.keys())

	def get_input(interface):
		inp = interface.request.recv(1024).strip().decode()
		return inp

	def print(interface, message):
		interface.request.sendall(message.encode())

	def handle(interface):
		interface.print('Welcome in the HideAndSec secret VPS ! [Location : Paris, France]\n')
		loaded_commands = interface.get_loaded_commands()
		interface.print(f"[+] Vipère v1.26 loaded !\n~ Currently loaded functions : [{', '.join(loaded_commands)}]\n\n")
		while True:
			interface.print('Which function do you want to launch ?\nExample : Bonjour {whoami}, il est actuellement {get_time} !\n=> ')

			text = interface.get_input()
			requested_commands = [fname for _, fname, _, _ in Formatter().parse(text) if fname]
			secure_commands = SecureCommands(requested_commands)
			try:
				interface.print(text.format(**secure_commands.dispatcher))
				interface.print("\n\n")
			except KeyError:
				interface.print("You tried to hack us, huh ?!\nWe're secure, try harder.\n")
			except BrokenPipeError:
				pass
			except Exception:
				interface.print("Some exception happened.\n")

class SecureCommands():

	def __init__(self, requested_commands):
		self.requested_commands = requested_commands

		# I saw this post which was saying that using a dispatcher to use
		# functions from a dictionary is pretty safe
		# https://softwareengineering.stackexchange.com/a/182095

		self.dispatcher = {
			"whoami": self.whoami,
			"get_time": self.get_time,
			"get_version": self.get_version
		}

		self.verify_commands()
	
	def verify_commands(self):
		for cmd in self.requested_commands:
			if cmd == "debug":
				import pdb; pdb.set_trace()
			if cmd in self.dispatcher and callable(self.dispatcher[cmd]):
				#print(self.dispatcher[cmd])
				self.dispatcher[cmd] = self.dispatcher[cmd]()
				#print(self.dispatcher[cmd])
				# To optimize resources, we only call functions when they are requested

	def whoami(self):
		output = subprocess.check_output("whoami")
		return output.decode().strip()

	def get_time(self):
		return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	def get_version(self):
		return sys.version.replace('\n', '')

	def get_infected(self):
		bridge = server.bridge
		#bridge.db.connect()
		#return bridge.db.total_infected

class SecureBridge():
	def __init__(self):
		#import database
		#self.db = database.SecureDatabase()
		return None

class ServerContext(socketserver.ThreadingTCPServer):
	def __init__(self, server_address, RequestHandlerClass) -> None:
		self.bridge = SecureBridge()
		self.allow_reuse_address = True
		return super().__init__(server_address, RequestHandlerClass)

	def handle_request(self) -> None:
		#self.bridge.db.update()
		return super().handle_request()

if __name__ == "__main__":
	address = ("0.0.0.0", 1337)

	with ServerContext(address, Station) as server:
		while True:
			server.handle_request()
