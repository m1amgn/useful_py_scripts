# Get Your API: https://www.remove.bg/tools-api
# pip install remove-bg-api

from remove_bg_api import RemoveBg


# Remove from File
bg = RemoveBg("Your API")  
img = bg.remove_bg_file(input_path="img.jpg", out_path="out.jpg")

# Remove from URL
img_url = "https://www.example.com/img"
img = bg.remove_background_from_img_url(input_url=img_url, out_path="out.jpg")
