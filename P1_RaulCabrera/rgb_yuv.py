"""""
Exercise 1:
Translator to convert 3 values in RGB into 3 values in YUV (YCbCr).
Also opposite operation.
Conversion operations extracted from:
https://softpixel.com/~cwright/programming/colorspace/yuv/
Check values at:
https://www.mikekohn.net/file_formats/yuv_rgb_converter.php
"""""


# Function to convert from RGB to YUV values
def rgb_2_yuv(r: int, g: int, b: int):

    y = 0.299 * r + 0.587 * g + 0.114 * b
    u = -0.1687 * r - 0.3313 * g + 0.5 * b + 128
    v = 0.5 * r - 0.4187 * g - 0.0813 * b + 128

    yuv = [y, u, v]
    # if value is negative or greater than 255, it takes min or max possible
    for i in range(0, 3):
        if yuv[i] < 0:
            yuv[i] = 0
        if yuv[i] > 255:
            yuv[i] = 255

    y_value = int(yuv[0])
    u_value = int(yuv[1])
    v_value = int(yuv[2])

    return y_value, u_value, v_value


# Function to convert from YUV to RGB values
def yuv_2_rgb(y: int, u: int, v: int):

    r = y + 1.4075 * (v - 128)
    g = y - 0.3455 * (u - 128) - 0.7169 * (v - 128)
    b = y + 1.779 * (u - 128)

    rgb = [r, g, b]

    for i in range(0, 3):
        if rgb[i] < 0:
            rgb[i] = 0
        if rgb[i] > 255:
            rgb[i] = 255

    r_value = int(rgb[0])
    g_value = int(rgb[1])
    b_value = int(rgb[2])

    return r_value, g_value, b_value


# Values must be 8-bit unsigned integers (0 to 255): color values

# Test yuv_2_rgb function
y1 = 100
u1 = 50
v1 = 180

r1, g1, b1 = yuv_2_rgb(y1, u1, v1)
print(r1, g1, b1)

# Test rgb_2_yuv function
r2 = 128
g2 = 128
b2 = 200

y2, u2, v2 = rgb_2_yuv(r2, g2, b2)
print(y2, u2, v2)

