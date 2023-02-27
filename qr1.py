import qrcode
data= "Welcome to Python projects" # we can give website link, email,etc..
img=qrcode.make(data)
img.save("qr1.jpg")