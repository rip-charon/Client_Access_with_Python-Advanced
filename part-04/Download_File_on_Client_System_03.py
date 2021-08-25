#CHARON :
# simple server socket program for gtting .txt file content from client and make the file

from socket import *

server = "0.0.0.0"
port = 5050
ADDR = (server,port)

s = socket(AF_INET, SOCK_STREAM)
s.bind((ADDR))
s.listen(5)

c, address = s.accept()

f = open("text.txt" , "w")

data = c.recv(1024).decode("utf-8")

f.write(data)

f.close()
s.close()