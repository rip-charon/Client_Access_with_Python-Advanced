# CHARON
# socket program for creating UDP server for send and recive data

from socket import *

s = socket(AF_INET , SOCK_DGRAM)

server = "0.0.0.0"

port = 5050

ADDR = (server,port)

s.bind((ADDR))

print("[+] server is running on port 5050 \n")

c , adrr = s.recvfrom(1025)

print("[+] connected to %s \n" % str(adrr))

print("[+] recived : %s " % str(c))

s.sendto("hello i am server !".encode('utf-8'), adrr)

s.close()