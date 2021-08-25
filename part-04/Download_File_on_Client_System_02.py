#CHARON :
# simple client socket program for reading .txt file content and send it to server

from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("192.168.1.115", 5050))

f = open("text.txt" , "r")

data = f.read()

s.send(data.encode('utf-8'))

f.close()
s.close()