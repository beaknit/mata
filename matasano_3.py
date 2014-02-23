
# 3. Single-character XOR Cipher
 
# The hex encoded string:
 
#       1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
 
# ... has been XOR'd against a single character. Find the key, decrypt the message.
 
# Write code to do this for you. How? Devise some method for "scoring" a piece of English plaintext. 
# (Character frequency is a good metric.) Evaluate each output and choose the one with the best score.
 
# Tune your algorithm until this works.

import string
import libmata

input_string = 'This is a string'

key_len = len(input_string)

#int_input = int('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736', 16)


# 1.  XOR the string against each char

# 1.1 Create the set of all alphas
alphas = list(string.ascii_letters)
numbers = list(string.digits)
alpha_nums = alphas + numbers

# 1.1.1 Pad to the length of the text to encrypt
raw_alpha_nums = [x * key_len for x in alpha_nums]

# 1.3 Encrypt plain text with list of keys
hexd_strings = [libmata.xor_encrypt(key=x, plain_text=input_string) for x in raw_alpha_nums]

# 2.  Print hex, key and decrypt

for x in range(len(hexd_strings)):
    print str(hexd_strings[x]) + " - " + str(raw_alpha_nums[x]) + " = " + libmata.xor_decrypt(key=raw_alpha_nums[x], hex_text=hexd_strings[x])
