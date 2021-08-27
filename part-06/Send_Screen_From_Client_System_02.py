#CHARON :
# simple server socket program for getting all .png files content from client and make the .png files [upload center]

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
    f = open('file_'+ str(i)+".png",'wb') #open in binary
    print("[+] FILE OPEN : file_"+ str(i)+".png")
    print("[+] Start receiveing")
    i=i+1
    while (True):       
    # receive data and write it to file
        l = sc.recv(1024)
        while (l):
            try:
                f.write(l)
                l = sc.recv(1024)
            except:
                sc.close()
                print("[+] Disconnected from %s !" % str(address))
                break
        print("[+] Received")
        f.close()
        print("[+] FILE CLOSE : file_"+ str(i)+".png")
        break

    print("[+] Waiting for new file...")

s.close()