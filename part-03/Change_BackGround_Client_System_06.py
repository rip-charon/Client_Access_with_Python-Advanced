# CHARON :
# socket program for changing windows background with given picture url from the web server side

from socket import *

ip = "0.0.0.0"
port = 5050

ADDR = (ip,port)

s = socket(AF_INET,SOCK_STREAM)
s.bind((ADDR))
s.listen(5)

print("[+] server is running on port 5050...")

c, address = s.accept()

print("[+] connected to the %s !" % str(address))
print("[+] For Test Enter This Link : http://192.168.1.115/pic.jpg ")

image = input("[+] Enter picture link : ")

s.sendall(image.encode('utf-8')) # copy this picture in the client system

print(c.recv(1024).decode('utf-8'))

c.close()