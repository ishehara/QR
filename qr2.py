import qrcode
qr = qrcode.QRCode(border=5, box_size=20)
qr.add_data("pathway to be come a pyhton expert")
qr.make(fit=True)
img=qr.make_image(fill_color="blue", back_color="white")
img.save("qr3.jpg")