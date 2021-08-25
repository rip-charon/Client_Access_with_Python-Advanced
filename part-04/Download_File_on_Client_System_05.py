#CHARON :
# simple server socket program for grtting .txt file content from client and make the file

import socket

server = "0.0.0.0"
port = 5050
ADDR = (server,port)

s = socket.socket()
s.bind((ADDR))
s.listen(10) # Accepts up to 10 connections.

while True:
    sc, address = s.accept()

    print(address)
    i=1
    f = open("jpg.jpg",'wb') #open in binary
    i=i+1
    while (True):       
    # receive data and write it to file
        l = sc.recv(1024)
        while (l):
                f.write(l)
                l = sc.recv(1024)
    f.close()


    sc.close()

s.close()