# pip install rembg Pillow

from rembg import remove
from PIL import Image

input_path = 'image.png'
background_path = 'background.jpg'
output_path = 'image_output.png'

open_image = Image.open(input_path)
output = remove(open_image)

background = Image.open(background_path)

background = background.resize(output.size)

background.paste(output, (0, 0), output)

background.save(output_path)
