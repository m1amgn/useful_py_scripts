from rembg import remove
from PIL import Image


input_path = "input_img.jpg"
output_path = "output_img.png"

input_img = Image.open(input_path)
output_img = remove(input_img)
output_img.save(output_path)
