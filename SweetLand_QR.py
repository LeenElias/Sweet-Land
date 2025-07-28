import qrcode
data="http://sweetland.menus.run/"
img=qrcode.make(data)
img.save("SweetLand_QR.png")