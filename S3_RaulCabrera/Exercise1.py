import os

# CUT VIDEO TO 10 SECONDS
"""""
Since encoding BBB video to AV1 (especially) takes a lot of time, we are going to cut the video to 10 seconds,
to get faster operations.
"""""

shortBBB = 'ffmpeg -i BBB.mp4 -ss 00:01:00 -t 00:00:10 -c:v copy -c:a copy shortBBB.mp4'
os.system(shortBBB)


# ENCODER VP8
"""""
libvpx is the VP8 video encoder for WebM.

We can encode the BBB video with two different MODES, depending on the bitrate.

CONSTANT BITRATE ENCODING MODE:
Encoding of the video in such a way that an average bitrate is reached.
This mode does not ensures that every frame is encoded with same amount of bits, since it could have
an effect on the quality. 
We need to set all options (minrate, maxrate and b:v) to the same value (bitrate will be constrained).
"""""

# vp8 = 'ffmpeg -i shortBBB.mp4 -c:v libvpx -minrate 500k -maxrate 500k -b:v 500k -c:a libvorbis outVP8.webm'
# os.system(vp8)

"""""
VARIABLE BITRATE ENCODING MODE:
Encoding of the video in such a way that a 'target bitrate' is reached on average.
There's also a CONSTANT QUALITY MODE (with CRF parameter) that makes every frame get a certain number of bits
so a certain quality level is achieved.
The CRF value goes from 4 to 63.
vp8 = 'ffmpeg -i shortBBB.mp4 -c:v libvpx -crf 10 -b:v 500k -c:a libvorbis outVP8.webm'
"""""

vp8 = 'ffmpeg -i shortBBB.mp4 -c:v libvpx -b:v 500k -c:a libvorbis outVP8.webm'
os.system(vp8)


# ENCODER VP9
"""""
To encode the BBB video, we can also use the two previously mentioned modes:

VARIABLE BITRATE: 'ffmpeg -i shortBBB.mp4 -c:v libvpx-vp9 -b:v 500K outVP9.webm'

CONSTANT BITRATE: 'ffmpeg -i shortBBB.mp4 -c:v libvpx-vp9 -minrate 500K -maxrate 500K -b:v 500K outVP9.webm'
"""""

vp9 = 'ffmpeg -i shortBBB.mp4 -c:v libvpx-vp9 -b:v 500k outVP9.webm'
os.system(vp9)


# ENCODER H265
"""""
To encode the BBB video h.265, we can use the following command, where:
    - option '-c:v libx265 -vtag hvc1' is used to select compression.
    - option '-c:a copy' is used to copy audio in output without any compression.
    - option '-vtag hvc1' indicates use of codec HVC1 (or h.265) during conversion.
"""""

h265 = 'ffmpeg -i shortBBB.mp4 -c:v libx265 -vtag hvc1 -c:a copy outH265.mp4'
os.system(h265)


# ENCODER AV1
"""""
Needed to enable libaom (libaom-av1) during compilation of ffmpeg.
As in previous cases, libaom offers AVERAGE BITRATE MODE (target) in which specified bitrate is reached,
on average.
Conversion takes a lot of time to be done.
"""""
av1 = 'ffmpeg -i shortBBB.mp4 -c:v libaom-av1 -b:v 500k outAV1.mkv'
os.system(av1)


# SPLIT-SCREEN VIDEO OF THE 4 CONVERTED VIDEOS

# SCALING 4 VIDEOS TO RESOLUTION: 720p
split = 'ffmpeg -i outAV1.mkv -i outH265.mp4 -i outVP8.webm -i outVP9.webm -filter_complex "[0]scale=-1:720[v0];' \
        '[1]scale=-1:720[v1];[2]scale=-1:720[v2];[3]scale=-1:720[v3];[v0][v1][v2][v3]xstack=inputs=4:' \
        'layout=0_0|w0_0|0_h0|w0_h0[v]" -map "[v]" output720.mp4'
os.system(split)

# SCALING 4 VIDEOS TO RESOLUTION: 480p
split = 'ffmpeg -i outAV1.mkv -i outH265.mp4 -i outVP8.webm -i outVP9.webm -filter_complex "[0]scale=480:-1[v0];' \
        '[1]scale=480:-1[v1];[2]scale=480:-1[v2];[3]scale=480:-1[v3];[v0][v1][v2][v3]xstack=inputs=4:' \
        'layout=0_0|w0_0|0_h0|w0_h0[v]" -map "[v]" output480.mp4'
os.system(split)

# SCALING 4 VIDEOS TO RESOLUTION: 360x240
split = 'ffmpeg -i outAV1.mkv -i outH265.mp4 -i outVP8.webm -i outVP9.webm -filter_complex "[0]scale=360:240[v0];' \
        '[1]scale=360:240[v1];[2]scale=360:240[v2];[3]scale=360:240[v3];[v0][v1][v2][v3]xstack=inputs=4:' \
        'layout=0_0|w0_0|0_h0|w0_h0[v]" -map "[v]" output360x240.mp4'
os.system(split)

# SCALING 4 VIDEOS TO RESOLUTION: 160x120
split = 'ffmpeg -i outAV1.mkv -i outH265.mp4 -i outVP8.webm -i outVP9.webm -filter_complex "[0]scale=160:120[v0];' \
        '[1]scale=160:120[v1];[2]scale=160:120[v2];[3]scale=160:120[v3];[v0][v1][v2][v3]xstack=inputs=4:' \
        'layout=0_0|w0_0|0_h0|w0_h0[v]" -map "[v]" output160x120.mp4'
os.system(split)

"""""
RESULT
In the resulting video we can observe:
        - Top left: outAV1.mkv video
        - Top right: outH265.mp4 video
        - Bottom left: outVP8.webm video
        - Bottom right: outVP9.webm video
"""""
