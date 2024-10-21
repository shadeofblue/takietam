import ctypes
from ctypes.util import find_library

# Load the libcrypto library
libcrypto_path = find_library('crypto')
if not libcrypto_path:
    raise Exception('libcrypto not found')
libcrypto = ctypes.CDLL(libcrypto_path)

# Define the function prototype
# The SHA256 function takes three parameters: the data to hash, the length of the data, and the output buffer
libcrypto.SHA256.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t, ctypes.POINTER(ctypes.c_ubyte)]
libcrypto.SHA256.restype = ctypes.POINTER(ctypes.c_ubyte)

# Prepare the data to hash
data = b"Hello, world!"
data_length = len(data)
data_array = (ctypes.c_ubyte * data_length)(*data)

# Prepare the output buffer (32 bytes for SHA-256)
buffer = (ctypes.c_ubyte * 32)()

# Call the SHA256 function
result = libcrypto.SHA256(data_array, data_length, buffer)

# Convert the result to a hexadecimal string
hex_digest = ''.join(format(x, '02x') for x in buffer)

print(hex_digest)
