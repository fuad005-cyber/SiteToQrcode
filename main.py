import qrcode
image = qrcode.make('url') #Add a website url
image.save("qr.png")
