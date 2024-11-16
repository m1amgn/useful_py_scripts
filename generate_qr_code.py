# Python QrCode
# pip install pyqrcode
# pip install pypng

import pyqrcode
import png

link = "https://medium.com/"

qr = pyqrcode.create(link)

# save in png
qr.png('qr.png', scale=6)

# save in svg
qr.svg('qr.svg', scale=6)

# save in png with low error correction
qr.png('qr_low.png', scale=6, module_color='red', background='white', quiet_zone=1)


#or
import qrcode

input_URL = "https://www.google.com/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr.add_data(input_URL)
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")
img.save("url_qrcode.png")

print(qr.data_list)
