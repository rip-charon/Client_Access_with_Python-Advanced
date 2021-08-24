# CHARON :
# urlib program for download picture from given server

import urllib.request

image_url = 'http://192.168.1.115/pic.jpg' #the image on the web
save_name = 'my_image.jpg' #local name to be saved
urllib.request.urlretrieve(image_url, save_name)