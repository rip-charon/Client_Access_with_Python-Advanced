# CHARON
# socket program for creating UDP client for send and recive data

from socket import *

s = socket(AF_INET , SOCK_DGRAM)

s.sendto("[-] client >> hello i am the udp client ".encode('utf-8'),("192.168.1.15",5050))

data = s.recv(1024)

print(data)

s.close()