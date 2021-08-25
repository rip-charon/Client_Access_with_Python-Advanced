import socket                   

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       

s.connect(("192.198.1.115", 5050))
s.send("Hello server!".encode('utf-8'))

with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')