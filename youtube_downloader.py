import pytube


link = input('Enter youtube video url: ')

yt = pytube.YouTube(link)

yt.streams.first().download()

print('Done')
