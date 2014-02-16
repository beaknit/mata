
# 3. Single-character XOR Cipher
 
# The hex encoded string:
 
#       1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
 
# ... has been XOR'd against a single character. Find the key, decrypt the message.
 
# Write code to do this for you. How? Devise some method for "scoring" a piece of English plaintext. 
# (Character frequency is a good metric.) Evaluate each output and choose the one with the best score.
 
# Tune your algorithm until this works.

import string
import binascii

base_int = int(binascii.hexlify('This is a string'), 16)

#first_int = int('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736', 16)

first_int = base_int

# 1.  XOR the string against each char

# 1.1 Create the set of all alphas
alphas = list(string.ascii_letters)
numbers = list(string.digits)

alpha_nums = alphas + numbers

# 1.2 Convert that ascii to hex
hex_alpha_nums = [binascii.hexlify(x) for x in alpha_nums]

# 1.3 XOR hex with hexstring
xord_strings = [first_int ^ int(x,16) for x in hex_alpha_nums]

hexd_strings = [ '%x' % x for x in xord_strings]

# 2.  unhex it (binascii.unhexlify)

unhexd_strings = [binascii.unhexlify(x) for x in hexd_strings]