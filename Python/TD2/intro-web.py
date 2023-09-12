import socket

host = "www.oteria.fr"
port = 80
s = socket.socket()
s.connect((host, port))
s.send(b"GET index.html HTML/1.1\r\n")
data = s.recv(128)
print(data.decode())
s.close()