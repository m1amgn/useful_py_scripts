# pip install moviepy

from moviepy.editor import VideoFileClip


def compress_video(input_file, output_file, target_bitrate):
    # Загрузка видеофайла
    video = VideoFileClip(input_file)
    # Изменение размера видео до высоты 360 пикселей
    video = video.resize(height=360)
    # Запись сжатого видеофайла с указанным битрейтом и кодеком "libx264"
    video.write_videofile(output_file, bitrate=target_bitrate, codec="libx264")


# Сжатие видео "video.mp4" и сохранение его в файле "output_video.mp4" с целевым битрейтом "1000k"
compress_video("video.mp4", "output_video.mp4", "1000k")
