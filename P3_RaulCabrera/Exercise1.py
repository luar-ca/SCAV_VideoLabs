import os

"""""
Exercise 1:
Create script to invoke ffmpeg to create a HLS transport stream container with BBB video.

Solution from:
https://ottverse.com/hls-packaging-using-ffmpeg-live-vod/#Live_HLS_Packaging_using_FFmpeg
"""""

"""""
Steps to HLS Packaging using ffmpeg:
1. read input video
2. scale/resize video to resolutions required
3. transcode scaled videos to required bitrate
4. transcode audio to required bitrate
5. combine video and audio, package each combination and create TS segments and playlists
6. create master playlist that points to each of the variants
"""""

# HLS Packaging
os.system('ffmpeg -i BBB.mp4 \
-filter_complex \
"[0:v]split=3[v1][v2][v3]; \
[v1]copy[v1out]; [v2]scale=w=1280:h=720[v2out]; [v3]scale=w=640:h=360[v3out]" \
-map [v1out] -c:v:0 libx264 -x264-params "nal-hrd=cbr:force-cfr=1" -b:v:0 5M -maxrate:v:0 5M -minrate:v:0 5M -bufsize:v:0 10M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
-map [v2out] -c:v:1 libx264 -x264-params "nal-hrd=cbr:force-cfr=1" -b:v:1 3M -maxrate:v:1 3M -minrate:v:1 3M -bufsize:v:1 3M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
-map [v3out] -c:v:2 libx264 -x264-params "nal-hrd=cbr:force-cfr=1" -b:v:2 1M -maxrate:v:2 1M -minrate:v:2 1M -bufsize:v:2 1M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
-map a:0 -c:a:0 aac -b:a:0 96k -ac 2 \
-map a:0 -c:a:1 aac -b:a:1 96k -ac 2 \
-map a:0 -c:a:2 aac -b:a:2 48k -ac 2 \
-f hls \
-hls_time 2 \
-hls_playlist_type vod \
-hls_flags independent_segments \
-hls_segment_type mpegts \
-hls_segment_filename stream_%v/data%02d.ts \
-master_pl_name master.m3u8 \
-var_stream_map "v:0,a:0 v:1,a:1 v:2,a:2" stream_%v.m3u8')

"""""
Description of the steps

STEP 1 & 2:
[0:v] refers to the input's video stream and this is split into 3 outputs [v1], [v2], [v3].
[v1out], [v2out], [v3out] are variables that contain the output of the scaling process.


STEP 3 & 4:
We take the three variables [v1out], [v2out], and [v3out] and transcode each one of them using
libx264 at the desired bitrate.
-keyint_min value is set to 48 which should force a keyframe periodically.


STEP 5:
Some of the important settings that are needed for HLS packaging:

    hls_playlist_type=vod : ffmpeg creates a VOD playlist
    
    hls_time seconds : sets the target segment length in seconds
    (the segment will be cut on the next key frame after this time has passed - 2s)
    
    hls_segment_type : creates TS segments
    
    hls_flags independent_segments : all segments of the playlist are guaranteed to start with a Key frame
    
    hls_segment_filename filename : names the segments that are created
    
    var_stream_map : combines the various video and audio transcodes to create the HLS playlists
    

STEP 6:
Master creation: file that lists the playlists of the individual variants that have been packaged using HLS
"""""
