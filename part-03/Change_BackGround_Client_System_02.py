# CHARON :
# socket program for changing windows background with given picture client side

from socket import *
import ctypes

s = socket(AF_INET, SOCK_STREAM)

s.connect(('192.168.1.115',5050))

SPI_SETDESKWALLPAPER = 20 

image = s.recv(1024).decode('utf-8')

ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image , 0)

s.sendall("changed background !".encode('utf-8'))

s.close()