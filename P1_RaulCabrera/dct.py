"""""
Exercise 5:
DCT function applied on input matrix.
"""""
import math

# dimensions of matrix we are going to apply DCT on
m = 4
n = 4

pi = 3.14


# Function to find DCT and print it.
# It replicates the structure of the mathematical model:
#       dct[u][v] = cu * cv * sum_x_y(mat[x][y] * cos[(x + 0.5) * u * pi/n] * cos[(y + 0.5) * v * pi/n])

def dct_transform(data):
    # definition of result, it will store the dct
    dct = []
    # to fill and initialize the result matrix with empty spaces [None]
    for i in range(m):
        dct.append([None for _ in range(n)])

    # iteration over matrix indexes
    for u in range(m):
        for v in range(n):
            # coefficients cu and cv:
            #       if u or v are 0 --> c = sqrt(1/m) and c = sqrt(1/n)
            #       otherwise --> c = sqrt(2/m) and c = sqrt(2/n)
            if u == 0:
                cu = (1 / m) ** 0.5
            else:
                cu = (2 / m) ** 0.5
            if v == 0:
                cv = (1 / n) ** 0.5
            else:
                cv = (2 / n) ** 0.5

            # we need to operate the sum operation iterating again over matrix indexes
            # variable to store sum:
            sum_xy = 0
            for x in range(m):
                for y in range(n):
                    # computation of the cosines
                    dct1 = data[x][y] * math.cos((x + 0.5) * u * pi/m) * math.cos((y + 0.5) * v * pi/n)
                    sum_xy += dct1
            # result of dct applying the formula structure
            dct[u][v] = cu * cv * sum_xy
            # printing
            print(dct[u][v], end="\t")

        print()


# Test DCT function with matrix 4x4
example_matrix = [[255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255], [255, 255, 255, 255]]
dct_transform(example_matrix)
