from socket import *

server = "0.0.0.0"
port = 5050
ADDR = (server,port)

s = socket(AF_INET, SOCK_STREAM)
s.bind((ADDR))
s.listen(5)                    

print('[+] Server listening on port 5050...')

while True:
    conn, addr = s.accept()     
    print('[+] Got connection from %s !'% str(addr))
    data = conn.recv(1024).decode('utf-8')
    print('[+] Server received', repr(data))

    filename = 'mytext.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()