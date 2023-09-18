from moviepy.editor import *


def cut_video(input_file, start_time, end_time, output_file):
  '''time in sec'''
    video = VideoFileClip(input_file)
    trimmed_video = video.subclip(start_time, end_time)
    trimmed_video.write_videofile(output_file, codec="libx264", audio_codec="aac")

cut_video("1.mp4", 300, 3264, "1-cutted.mp4")
