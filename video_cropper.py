# Crop Video 
# pip install moviepy

from moviepy.editor import *

# x1, y1 is the top left corner of the crop
# x2, y2 is the bottom right corner of the crop

filename = 'test.mp4'
clip = VideoFileClip(filename)
clip = clip.crop(x1=250, y1=150, x2=clip.width, y2=clip.height)
clip.write_videofile("test_crop.mp4")
