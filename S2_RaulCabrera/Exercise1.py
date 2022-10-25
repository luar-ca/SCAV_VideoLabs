import os
import datetime

"""""
Exercise 1: Cut N seconds from BBB video. N seconds provided by user.
"""""


# Give number of seconds from start to n (user input)
n = input('Give a number of seconds: ')

if n.isdigit():
    secs = int(n)
    print('Thank you')
    # To format time value, datetime is defined with following arguments (year, month, day, hour, minute, second)
    start = datetime.datetime(1, 1, 1, 00, 00, 00)
    # Sum of 00 time and seconds provided by user
    finish = start + datetime.timedelta(seconds=secs)
    # Convert time values of vide start and finish to string
    vid_start = str(start.time())
    vid_finish = str(finish.time())
    # Add strings to command and call ffmpeg to cut the video
    command = 'ffmpeg -ss ' + vid_start + ' -to ' + vid_finish + ' -i big_buck_bunny.mp4 -c copy cutNsec_bbb.mp4'
    os.system(command)
else:
    # System asks for an integer of seconds, if not:
    print('The introduced value is not valid. Please, give an INTEGER value')

