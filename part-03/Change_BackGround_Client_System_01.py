# CHARON :
# program for changing windows background with given picture

import ctypes

SPI_SETDESKWALLPAPER = 20 

ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "image.jpg" , 0)