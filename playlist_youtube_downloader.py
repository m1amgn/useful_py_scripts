from pytube import Playlist
 
playlist = Playlist("https://www.youtube.com/playlist?example")
 
print(f"Download: {playlist.title}")
for video in playlist.videos:
    video.streams.first().download()
    print(f"Video {video.title} downloaded")
