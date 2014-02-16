
# 3. Single-character XOR Cipher
 
# The hex encoded string:
 
#       1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
 
# ... has been XOR'd against a single character. Find the key, decrypt the message.
 
# Write code to do this for you. How? Devise some method for "scoring" a piece of English plaintext. 
# (Character frequency is a good metric.) Evaluate each output and choose the one with the best score.
 
# Tune your algorithm until this works.

import string
import binascii

input_string = 'This is a string'

int_input = int(binascii.hexlify(input_string), 16)

reg_len = len(input_string)

#int_input = int('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736', 16)


# 1.  XOR the string against each char

# 1.1 Create the set of all alphas
alphas = list(string.ascii_letters)
numbers = list(string.digits)

alpha_nums = alphas + numbers

raw_alpha_nums = [x * reg_len for x in alpha_nums]

# 1.2 Convert that ascii to hex
hex_alpha_nums = [binascii.hexlify(x) for x in raw_alpha_nums]

int_alpha_nums = [int(x,16) for x in hex_alpha_nums]

# 1.3 XOR int of input_string with int of hex_alpha_nums
xord_int_strings = [int_input ^ x for x in int_alpha_nums]

hexd_strings = [ '%x' % x for x in xord_int_strings]

# 2.  unhex it (binascii.unhexlify)

int_unhexd_strings = [int(x,16) for x in hexd_strings]

#dexord_int_strings = map(lambda l:, sequence)

for x in range(len(int_unhexd_strings)):
    print str(hexd_strings[x]) + " - " + str(raw_alpha_nums[x]) + " = " + str(binascii.unhexlify("%x" % (int_unhexd_strings[x] ^ int_alpha_nums[x])))
