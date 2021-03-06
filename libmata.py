
def hex2base64(hex_string=""):
    r'''Take in a hex string and return the Base64 equivalent (Prob 1)

    Arguments:
    :param hex_string: input string
    :type hex_string: binary hex string
    :returns: base64-encoded string

    >>> import libmata
    >>> libmata.hex2base64(hex_string=b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
    'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t\n'
    '''

    import binascii

    # convert chars to bytes
    bin_unhex = binascii.unhexlify(hex_string)

    # convert bytes to base64 and return it
    return binascii.b2a_base64(bin_unhex)


def fixed_xor(first_hex="", second_hex=""):
    r'''Take two hex strings and xor them (Prob 2)

    Arguments:
    :param first_hex: input string
    :type first: HEX string
    :param second_hex: input string
    :type second: HEX string
    :returns: hex string

    >>> import libmata
    >>> libmata.fixed_xor(first_hex=b'1c0111001f010100061a024b53535009181c', second_hex=b'686974207468652062756c6c277320657965')
    '746865206b696420646f6e277420706c6179'
    '''

    # recase hex to int so we can xor it
    first_int = int(first_hex, 16)
    second_int = int(second_hex, 16)

    hex_result = '%x' % (first_int ^ second_int)

    return hex_result


def xor_encrypt(key="", plain_text=""):
    r'''Accept a key and use it to xor encrypt a plain text string

    Arguments:
    :param key: Encryption key
    :type key: string
    :param plain_text: Text to encrypt
    :type plain_text: string
    :returns:  hex string

    >>> import libmata
    >>> libmata.xor_encrypt('PPPPPPPPPPPPPPPP','This is a string')
    '4383923703923703170232422393e37'
    '''
    int_key = string_to_int(key)

    int_text = string_to_int(plain_text)

    xord_int_strings = int_key ^ int_text

    hexd_string = '%x' % xord_int_strings

    return hexd_string


def xor_decrypt(key="", hex_text=""):
    r'''Accept a key and use it to xor decrypt an encrypted hex string

    Arguments:
    :param key: Encryption key
    :type key: string
    :param hex_text: Text to decrypt
    :type hex_text: HEX string
    :returns:  string

    >>> import libmata
    >>> libmata.xor_decrypt('PPPPPPPPPPPPPPPP','4383923703923703170232422393e37')
    'This is a string'
    '''
    import binascii

    int_key = string_to_int(key)

    int_text = hex_to_int(hex_text)

    xord_int_strings = int_key ^ int_text

    hex_string = "%x" % xord_int_strings

    plain_text = binascii.unhexlify(hex_string)

    return plain_text


def string_to_int(input):
    r'''Convert a string to an integer by way of hexadecimal

    Arguments:
    :param input: String to convert
    :type input: string
    :returns: integer OR long
    '''
    import binascii

    hex_input = binascii.hexlify(input)

    int_input = hex_to_int(hex_input)

    return int_input


def hex_to_int(input):
    r'''Convert a hex to an integer

    Arguments:
    :param input: HEX string to convert
    :type input: HEX string
    :returns: integer OR long
    '''
    int_input = int(input, 16)

    return int_input


def single_char_xor_cipher_with_quads(hex_input):
    r'''Single-character XOR Cipher (Problem 3)
    - Take a hex-encoded string
    - Read in ascii letters and top-1000 english quagrams
    - Run an xor_decrypt with single-char-based key
    - If quadram matches, test for white space
    - If white space matches, return the result

    Arguments:
    :param hex_input: HEX string to decrypt
    :type hex_input: HEX String
    :returns: decrypted base64-encoded string

    >>> import libmata
    >>> libmata.single_char_xor_cipher_with_quads('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    ('X', "XXXXXXXXXXXXXXXCooking MC's like a pound of bacon", "Cooking MC's like a pound of bacon", 'OUND', 'KING')
    '''
    import string
    import re

    stringslist = string.lowercase + string.uppercase + '0123456789'
    input_len = len(hex2base64(hex_input))
    with file('top_5000_english_quadgrams.txt') as f:
        quads = f.read().split("\n")

    for x in stringslist:
        decrypt = xor_decrypt(key=(x * input_len), hex_text=hex_input)
        # Decrypts tend to be padded and that can skew the matches
        # Create a pattern to detect key padding and strip it
        # This regex says "Match everything BUT a repeated string of the key"
        pad_pattern = "[^" + x + "*].*"
        cleaned_decrypt_match = re.search(pad_pattern, decrypt)
        cleaned_decrypt = cleaned_decrypt_match.group(0)
        for y in quads:
            if y in cleaned_decrypt.upper():
                if " " in cleaned_decrypt:
                    for z in quads:
                        if z in cleaned_decrypt.upper().replace(y, ''):
                            return (x, decrypt, cleaned_decrypt, y, z)


def detect_single_char_xor(filename):
    r'''Detect single-char XOR (Problem 4)
    - Take in a file of encrypted strings terminated by newline
    - Run the strings through the single-char xor decrypt
    - Find the decrypt using quadgrams

    Arguments:
    :param filename: File with newline-terminated ciphertext
    :type filename: newline-terminated file
    :returns:  Decrypted base64-encoded string

    >>> import libmata
    >>> libmata.detect_single_char_xor('detect_single_char_xor_test_set.txt')
    ('5', '55555555555Now that the party is jumping\n', 'Now that the party is jumping', 'THAT', 'PART')
    '''
    with file(filename) as f:
        s = f.read().split("\n")

    result = [single_char_xor_cipher_with_quads(x) for x in s]

    for x in result:
        if x:
            return x
