#import struct
import binascii

cstring = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

# store string in 96-byte struct
#s = struct.Struct('96s')
#packed_data = s.pack(cstring)



# convert chars to bytes
bin_unhex = binascii.unhexlify(cstring)

# convert bytes to base64 and print it
print binascii.b2a_base64(bin_unhex)


# reassemble base64 into string
# see binascii.b2a_base64(data)

