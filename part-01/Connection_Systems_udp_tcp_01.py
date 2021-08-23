# CHARON :
# socket program for creating server on port 5050 and send and recive data from client side.

from socket import *

s = socket(AF_INET,SOCK_STREAM)

server = "0.0.0.0"

port = 5050

ADDR = (server,port)

s.bind((ADDR))

s.listen(5)

print("[+] server start running on port 5050 \n")

client , addr = s.accept()

print("connected to %s \n " % str(addr))

client.sendall("hello i am server... ".encode('utf-8'))

data = client.recv(1024)

print(data)

client.close()