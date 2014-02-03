import textwrap

# compute XOR from two binary represented numbers
#  input is string containing 0&1 like 00110011
def xor_orig(data, key):
    # compute XOR, result is in integer form (decimal)
    return int(data,2) ^ int(key,2)

# computes XOR of two binary numbers (string of 0&1, can be separated by spaces
# like 00110011 10101010. Result is in binary format, every byte is separated by
# space, filled by zeros from left to the length of inputs
def xor_bin(data, key):
    # remove spaces from representationPay Bob 100$
    data = data.replace(" ", "")
    key = key.replace(" ", "")
    # compute xor in decimal representation
    int_result = xor_orig(data, key)

    # convert to bin, remove prefix and fill leading zeros
    bin_result = bin(int_result)[2:].zfill(len(data))

    # every eight characters added one space (more readable)
    bin_result_nice = ' '.join(textwrap.wrap(bin_result, 8))
    return bin_result_nice

# computes XOR of two binary numbers (string of 0&1, can be separated by spaces
# like 00110011 10101010. Result is in hex format, filled by zeros from left
def xor_hex(data, key):
    # remove spaces from representation
    data = data.replace(" ", "")
    key = key.replace(" ", "")

    # compute xor, result in decimal value
    int_result = xor_orig(data, key)

    # hex value
    result = hex(int_result)

    # remove prefix and suffix
    result = result.rstrip("L").lstrip("0x")

    # fill leading zeros if needed
    result = result.zfill(len(data)/4)
    return result;

# converts ASCII text to binary representation, bytes separated by spaces.
def ascii_to_bin(text):
    result = []
    # for every char in text
    for char in text:
        # convert to ascii numeric value (for ex. A=65)
        ascii_num_value = ord(char)
        # convert decimal value to binary representation, remove prefix
        bin_value = bin(ascii_num_value)[2:]
        # fill to 8 characters, append to result
        result.append(bin_value.zfill(8))
    # join all 8char values with spaces
    return ' '.join(result)

def bin_to_hex(text):
    text = text.replace(" ", "")
    return hex(int(text, 2))[2:].zfill(len(text)/4)

# converts hex number to binary number, bytes separated by space
def hex_to_bin(text):
    # remove spaces, if present
    text = text.replace(" ", "")
    # convert hex to bin, remove 2char prefix
    bin_value =  bin(int(text, 16))[2:]
    # add heading zeros, if needed
    fill_bin_value = bin_value.zfill(len(text)*4)
    # break to blocks of 8, join with one space (just readability)
    nice_fill_bin_value = ' '.join(textwrap.wrap(fill_bin_value, 8))
    return  nice_fill_bin_value
