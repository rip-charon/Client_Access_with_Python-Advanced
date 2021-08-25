#CHARON :
# simple client socket program for reading .txt file content and send it to server

from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("192.168.1.115", 5050))

f = open("text.txt" , "rb")

data = f.read().decode("utf-16")

s.send(data.encode('utf-8'))

f.close()
s.close()