import os

"""""
Exercise 3:
Script able to change resolution of any given input (use of minBBB.mp4 video from Exercise 2)
"""""


def resize_function(filename: str, height: int, width: int):
    h = str(height)
    w = str(width)

    if filename.find('.mp4') != -1:
        re_vid = 'ffmpeg -i ' + filename + ' -vf scale=' + w + ':' + h + ',setsar=1:1 re_vid.mp4'
        os.system(re_vid)
    else:
        re_img = 'ffmpeg -i ' + filename + ' -vf scale=' + w + ':' + h + ' re_img.jpg'
        os.system(re_img)


# Input is a jpg image
resize_function('lenna.jpg', 500, 100)

# Input is a mp4 video
resize_function('minBBB.mp4', 200, 400)
