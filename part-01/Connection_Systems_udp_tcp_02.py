# CHARON :
# socket program for creating client on port 5050 and send and recive data from server side.

from socket import *

s = socket(AF_INET,SOCK_STREAM)

s.connect(('192.168.1.115',5050))

print("[+] connected... \n")

data = s.recv(1024)

print(data)

s.send("client > hello i am the client... ".encode("utf-8"))

s.close()