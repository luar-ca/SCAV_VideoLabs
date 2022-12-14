from concurrent.futures import ProcessPoolExecutor
import os

"""""
Exercise 3:
Create script to livestream (local video) with ffmpeg.

Solution from:
https://stackoverflow.com/questions/43826675/how-to-live-stream-a-local-video-using-ffmpeg
"""""


def first_terminal():

    first = 'ffmpeg -i BBB.mp4 -v 0 -vcodec mpeg4 -f mpegts udp://127.0.0.1:23000'
    os.system(first)


def second_terminal():

    second = 'ffplay udp://127.0.0.1:23000'
    os.system(second)


# To execute separate processes concurrently, we use ProcessPoolExecutor
def main():

    with ProcessPoolExecutor(max_workers=2) as executor:
        executor.submit(first_terminal)

        executor.submit(second_terminal)


if __name__ == "__main__":
    main()
