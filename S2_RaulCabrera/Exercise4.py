import os

"""""
Exercise 4: Change stereo input into mono output and opposite operation.
"""""

# BBB VIDEO IS STEREO
# Using pan audio filter we can split stereo stream into two specific mono channels
# We obtain two videos, one for each audio mono channel:

# Right channel
right_cmd = 'ffmpeg -i big_buck_bunny.mp4 -af "pan=mono|c0=c1" right_bbb.mp4'
os.system(right_cmd)

# Left channel
left_cmd = 'ffmpeg -i big_buck_bunny.mp4 -af "pan=mono|c0=c0" left_bbb.mp4'
os.system(left_cmd)


# ONCE WE HAVE TWO MONO FILES
# We can merge the two previous mono files into a new stereo audio
# New stereo audio coincides with audio in BBB video

stereo_cmd = 'ffmpeg -i left_bbb.mp4 -i right_bbb.mp4 -filter_complex ' \
             '"[0:a][1:a]amerge=inputs=2[a]" ' \
             '-map "[a]" stereo_bbb.mp4'

os.system(stereo_cmd)
