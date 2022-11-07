import os

"""""
Exercise 1:
Script to parse input file: extraction of video metadata
"""""

filename = 'BBB.mp4'

cmd = 'ffprobe ' + filename
os.system(cmd)

"""""
RESULTS:
To get useful information about an input file we use 'ffprobe' command.
It provides a lot of relevant data about the input such as the number of video and audio streams, 
some codec details, bit rates or video/audio durations.
"""""
