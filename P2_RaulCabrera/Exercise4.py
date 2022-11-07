import os

"""""
Exercise 4:
Script to get information about audio streams of input video: mp4PACK.mp4 (video from Exercise 2)
Based on their codecs, we decide which broadcasting standard the video can fit in
"""""

# Command to count video/audio streams. Number of streams is read with 'os.popen(command).read()'
cmd = 'ffprobe mp4PACK.mp4 -show_entries format=nb_streams -v 0 -of compact=p=0:nk=1'
streams = os.popen(cmd).read()
print('Number of streams in mp4 video: ' + streams)


# First stream is video
# We select specific video stream with 'v:0'. We want to show 'codec_name' of video stream.
st0 = 'ffprobe -hide_banner -v panic -select_streams v:0 ' \
     '-show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 mp4PACK.mp4'
vid_st = os.popen(st0).read()

# Next streams are audio
# We select specific audio stream with 'a:0', 'a:1' and 'a:2'. We want to show 'codec_name' of audio streams.
st1 = 'ffprobe -hide_banner -v panic -select_streams a:0 ' \
     '-show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 mp4PACK.mp4'
au_st1 = os.popen(st1).read()

st2 = 'ffprobe -hide_banner -v panic -select_streams a:1 ' \
     '-show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 mp4PACK.mp4'
au_st2 = os.popen(st2).read()

st3 = 'ffprobe -hide_banner -v panic -select_streams a:2 ' \
     '-show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 mp4PACK.mp4'
au_st3 = os.popen(st3).read()

# Codec of every stream
print('Codec of video stream: ' + vid_st)
print('Codec of audio stream 1: ' + au_st1)
print('Codec of audio stream 2: ' + au_st2)
print('Codec of audio stream 3: ' + au_st3)
print('Video codec is H.264 and audio codecs are AAC and MP3\n' + 'The best broadcasting standard is DVB')
