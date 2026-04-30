import qrcode

text_or_url = input("Enter the text or url: ").strip()
filename = input("Enter the filename: ").strip()

qr = qrcode.QRCode()
qr.add_data(text_or_url)
image = qr.make_image(fill_color="black", back_color="white")
with open(filename, "wb") as f:
    image.save(f)
