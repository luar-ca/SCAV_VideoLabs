import os

"""""
Exercise 2:
New BBB container creation:
    - Cut BBB video into 1 min
    - Export 1 min video audio as MP3 stereo
    - Export 1 min video audio as AAC with lower bitrate
    - Package everything in MP4 container
"""""

# Cut video into 1 minute (mp4 as container format)
"""""
The command '-ss' specifies the starting time and '-t' specifies the duration from the start
The '-c:v copy -c:a copy' commands copy the original audio and video in the output file without re-encoding
"""""

minBBB = 'ffmpeg -i BBB.mp4 -ss 00:00:00 -t 00:01:00 -c:v copy -c:a copy minBBB.mp4'
os.system(minBBB)


# Export audio as MP3 STEREO (mp3 as container format)
"""""
When we extract audio track, we must use a container format for the final file
In this case, we choose the mp3 format

We are extracting audio with RE-ENCODING
Instead of copying the audio in output file, we need to specify the codec after '-acodec'

Command '-map 0:a' selects all audio streams from input file
We use 'libmp3lame' to encode audio streams from aac to mp3
"""""

mp3BBB = 'ffmpeg -i minBBB.mp4 -map 0:a -acodec libmp3lame mp3BBB.mp3'
os.system(mp3BBB)


# Export audio in AAC WITH LOWER BITRATE (acc as container format)
"""""
Fraunhofer FDK AAC codec library (libfdk_aac) is currently the highest-quality AAC encoder available with ffmpeg

Variable Bitrate (VBR)
Set the VBR quality with the -vbr flag: 1 is lowest quality and 5 is highest quality

Constant Bitrate (CBR)
Set a specific bit rate with the -b:a option
"""""

cbrBBB = 'ffmpeg -i minBBB.mp4 -c:a libfdk_aac -b:a 64k cbrBBB.aac'
os.system(cbrBBB)

vbrBBB = 'ffmpeg -i minBBB.mp4 -c:a libfdk_aac -vbr 1 vbrBBB.aac'
os.system(vbrBBB)


# Package everything in MP4 container
"""""
We add multiple audio streams to 1 min video
"""""

mp4PACK = 'ffmpeg -i minBBB.mp4 -i mp3BBB.mp3 -i cbrBBB.aac -map 0 -map 1 -map 2 -codec copy mp4PACK.mp4'
os.system(mp4PACK)
