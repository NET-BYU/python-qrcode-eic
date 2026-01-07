import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("Some data")
img = qr.make_image(fill_color="black", back_color="white")
img.save("before-eic.png")

# Can't add too much EIC data or the QR code will get corrupted (because of my naive approach)
qr.add_eic_data(b"EIC")

img = qr.make_image(fill_color="black", back_color="white")
img.save("after-eic.png")
