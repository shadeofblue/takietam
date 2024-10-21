from numba import jit
import ctypes

# Load the shared library
libcrypto = ctypes.CDLL("libcrypto.so")

# Assuming SHA256() is a function in the libcrypto library,
# define the function prototype in ctypes.
libcrypto.SHA256.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t, ctypes.POINTER(ctypes.c_ubyte)]
libcrypto.SHA256.restype = ctypes.POINTER(ctypes.c_ubyte)

# Define a wrapper function in Python that calls the C function
def call_sha256(data):
    buffer = (ctypes.c_ubyte * 32)()
    libcrypto.SHA256(data, len(data), buffer)
    return bytes(buffer)

# Numba JIT function that uses the wrapper
@jit(nopython=True)
def hash_data(data, func):
    # Call the external C function via the wrapper
    result = func(data)
    return result

# Convert Python data to ctypes and call the jitted function
data = (ctypes.c_ubyte * 13)(*b"Hello, world!")
hashed_data = hash_data(data, call_sha256)
print(hashed_data)
