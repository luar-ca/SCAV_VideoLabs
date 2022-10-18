"""""
Exercise 4:
Function that applies Run-Length Encoder to sequences of bits.
"""""

"""""
Run-length encoding algorithm is a type of compression in which:
    - input: sequence of characters (digit or non-digit) 
    - output: sequence of counts (for every char, number of times it appears in input sequence)
Compression is lossless.
"""""


def run_length_encoder(data_seq):
    # init of encoded seq, previous char variable and counter
    encoded = ''
    prev = ''
    count = 1
    # if there's no data, return empty
    if not data_seq:
        return 'EMPTY'
    # loop over each one of chars in data sequence
    for char in data_seq:
        # if consecutive characters don't match, add count and char
        if char != prev:
            # if there is previous, we use it
            if prev:
                encoded += str(count) + prev
            # if not, we define prev as the current char for next iteration
            count = 1
            prev = char
        else:
            # if they match, keep counting
            count += 1
    else:
        # return encoded sequence
        encoded += str(count) + prev
        return encoded


# Given an input sequence of bits, apply run length encoder
input_seq = '000000001111100001100011100000000'
encoded_val = run_length_encoder(input_seq)
print('Counts + Bit: ', encoded_val)





