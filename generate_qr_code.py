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
