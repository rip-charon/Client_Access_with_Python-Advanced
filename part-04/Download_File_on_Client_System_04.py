#CHARON :
# simple client socket program for reading .txt file content and send it to server

import socket

s = socket.socket()
s.connect(("192.168.1.115",5050))

f = open ("jpg.jpg", "rb")
l = f.read(1024)

while (l):
    s.send(l)
    l = f.read(1024)

s.close()