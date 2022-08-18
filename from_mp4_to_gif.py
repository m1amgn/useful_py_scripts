# Convert Video to Gif

# pip install moviepy

import moviepy.editor as mpy

def video_to_gif(videofile):
    clip = mpy.VideoFileClip(videofile)
    clip.write_gif("test.gif")
    clip.close()
    
video_to_Gif("test.mp4")
