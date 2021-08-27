#CHARON :
# simple server socket program for getting all .png files content from client and make the .png files [upload center]

import socket

server = "0.0.0.0"
port = 5050
ADDR = (server,port)

s = socket.socket()
s.bind((ADDR))
s.listen(10) # Accepts up to 10 connections.

i=1

print("[+] Server start running on port 5050")

while True:
    sc, address = s.accept()

    print("[+] Connected to %s !" % str(address))

    f = open('file_'+ str(i)+".png",'wb') #open in binary
    print("[+] FILE OPEN : file_"+ str(i)+".png")
    print("[+] Start receiveing")
    while (True):       
    # receive data and write it to file
        l = sc.recv(1024)
        while (l):
            try:
                f.write(l)
                l = sc.recv(1024)
            except:
                break
        print("[+] Received")
        f.close()
        print("[+] FILE CLOSE : file_"+ str(i)+".png")
        break

    sc.close()
    print("[+] Disconnected from %s !" % str(address))
    print("[+] Waiting for new file...")
    i=i+1

s.close()