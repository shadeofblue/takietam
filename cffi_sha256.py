from cffi import FFI

ffi = FFI()

# Load the OpenSSL libcrypto library
libcrypto = ffi.dlopen("libcrypto.so")

# Define the functions and types we need
ffi.cdef("""
typedef unsigned char *SHA256(const unsigned char *d, size_t n, unsigned char *md);
""")

# Prepare the data you want to hash
data = b"Hello, world!"
data_buffer = ffi.new("unsigned char[]", data)
hash_buffer = ffi.new("unsigned char[32]")  # SHA-256 hash size

# Call the SHA256 function
hash_result = libcrypto.SHA256(data_buffer, len(data), hash_buffer)

# Convert the resulting bytes to a hexadecimal string
hex_digest = ''.join("{:02x}".format(hash_buffer[i]) for i in range(32))

print(hex_digest)