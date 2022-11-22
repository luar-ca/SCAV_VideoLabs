import tkinter as tk
import os

"""""
Run first Exercise1.py to get shortBBB.mp4 video.
"""""


def onclick1():
    print("CONVERTING MP4 VIDEO TO VP8")
    vp8 = 'ffmpeg -i shortBBB.mp4 -c:v libvpx -b:v 500k -c:a libvorbis clickVP8.webm'
    os.system(vp8)
    print("VP8 VIDEO DONE")


def onclick2():
    print("CONVERTING MP4 VIDEO TO VP9")
    vp9 = 'ffmpeg -i shortBBB.mp4 -c:v libvpx-vp9 -b:v 500k clickVP9.webm'
    os.system(vp9)
    print("VP9 VIDEO DONE")


def onclick3():
    print("CONVERTING MP4 VIDEO TO H265")
    h265 = 'ffmpeg -i shortBBB.mp4 -c:v libx265 -vtag hvc1 -c:a copy clickH265.mp4'
    os.system(h265)
    print("H265 VIDEO DONE")


def onclick4():
    print("CONVERTING MP4 VIDEO TO AV1")
    av1 = 'ffmpeg -i shortBBB.mp4 -c:v libaom-av1 -b:v 500k clickAV1.mkv'
    os.system(av1)
    print("AV1 VIDEO DONE")


# Window
root = tk.Tk()
root.geometry('400x200')
root.title("CONVERSION MENU")

lab = tk.Label(root, text="Choose Codec to Convert BBB Video")
lab.pack()

# Button Elements
btn1 = tk.Button(root, text="VP8", command=onclick1)
btn2 = tk.Button(root, text="VP9", command=onclick2)
btn3 = tk.Button(root, text="H265", command=onclick3)
btn4 = tk.Button(root, text="AV1", command=onclick4)

# Put Element on Window
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()

root.mainloop()
