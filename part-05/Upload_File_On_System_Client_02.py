from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("192.168.1.115", 5050))

s.send("Hello server! Send me a file !".encode('utf-8'))

with open('mynewtext.txt', 'wb') as f:
    
    while True:
        data = s.recv(1024)
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
s.close()