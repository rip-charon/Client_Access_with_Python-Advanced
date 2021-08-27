from socket import *

server = "0.0.0.0"
port = 5050
ADDR = (server,port)

s = socket(AF_INET, SOCK_STREAM)
s.bind((ADDR))
s.listen(5)

print("[+] Server start running at port 5050... ")

c, address = s.accept()

print("[+] Connected to %s !" % str(address))

data = c.recv(10241024).decode("utf-8")

print(data)