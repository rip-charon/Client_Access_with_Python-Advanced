# CHARON :
# socket program for changing windows background with given picture server side

from socket import *

ip = "0.0.0.0"
port = 5050

ADDR = (ip,port)

s = socket(AF_INET,SOCK_STREAM)
s.bind((ADDR))
s.listen(5)

c, address = s.accept()

s.sendall("image.jpg".encode('utf-8'))

print(c.recv(1024).decode('utf-8'))

c.close()