from PIL import Image
from pyzbar import pyzbar

img = Image.open("qr1.jpg")
out = pyzbar.decode(img)
print(out[0][0].decode('utf-8'))

