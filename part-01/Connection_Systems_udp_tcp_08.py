# CHARON :
# socket program for creating client on port 1234 for chatting in udp connection with server

from socket import *

print("[+] client chat is running : ")

name = input("[+] Enter your name : ")

s = socket(AF_INET, SOCK_DGRAM)

print("connected to server \n")

while True:

    data = s.recv(1024)
    print(data.decode('utf-8'))
    print("\n")
    sms = input("[+] you >> ")
    cms = "[+] %s >> %s}" % (name,sms)
    s.sendto(cms.encode('utf-8'),("192.168.1.123",1234))
    print("\n")

s.close()