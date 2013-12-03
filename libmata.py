
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

def hexor(first_hex="", second_hex=""):
    r'''Take two hex strings and xor them

    Arguments:
    :param first: input string
    :type first: hex string
    :param second: input string
    :type second: hex string
    :returns: hex string

    >>> import libmata
    >>> libmata.hexor(first_hex=b'1c0111001f010100061a024b53535009181c', second_hex=b'686974207468652062756c6c277320657965')
    '0x746865206b696420646f6e277420706c6179L'
    '''

    # recase hex to int so we can xor it
    # first_int = int("1c0111001f010100061a024b53535009181c",16)
    # second_int = int("686974207468652062756c6c277320657965",16)

    first_int = int(first_hex,16)
    second_int = int(second_hex,16)

    return hex(first_int ^ second_int)
