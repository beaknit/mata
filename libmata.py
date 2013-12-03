
def hex2base64(hex_string=""):
    r'''Take in a hex string and return the Base64 equivalent (Prob 1)

    Arguments:
    :param hex_string: input string
    :type hex_string: binary hex string
    :returns: base64-encoded string

    >>> import libmata
    >>> libmata.hex2base64(b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
    'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t\n'
    
    '''

    import binascii

    # convert chars to bytes
    bin_unhex = binascii.unhexlify(hex_string)

    # convert bytes to base64 and return it
    return binascii.b2a_base64(bin_unhex)
