#CHARON :
# simple server socket program for getting all .jpg files content from client and make the .jpg files [upload center]

import socket

server = "0.0.0.0"
port = 5050
ADDR = (server,port)

s = socket.socket()
s.bind((ADDR))
s.listen(10) # Accepts up to 10 connections.

print("[+] Server start running on port 5050")

while True:
    sc, address = s.accept()

    print("[+] Connected to %s !" % str(address))

    i=1
    f = open('file_'+ str(i)+".jpg",'wb') #open in binary
    i=i+1
    while (True):       
    # receive data and write it to file
        l = sc.recv(1024)
        while (l):
            try:
                f.write(l)
                l = sc.recv(1024)
            except:
                break
    f.close()


    sc.close()

s.close()