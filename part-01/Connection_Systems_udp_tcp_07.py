# CHARON
# socket program for creating server on port 1234 for chatting in udp connection with client

from socket import *

s = socket(AF_INET , SOCK_DGRAM)

server = "0.0.0.0"

port = 1234

ADDR = (server,port)

s.bind((ADDR))

print("[+] server chat is running : ")

name = input("[+] Enter your name : ")

c , ADDR2 = s.recvfrom(1024)

print("[+] connected to %s \n" % str(ADDR2))

while True:

    sms = input("[+] you >> ")
    cms = "[+] %s >> %s" % (name,sms)
    s.sendto(sms.encode('utf-8'),ADDR2)
    print("\n")
    data = c.recv(1024)
    print(data.decode('utf-8'))
    print("\n")

c.close()