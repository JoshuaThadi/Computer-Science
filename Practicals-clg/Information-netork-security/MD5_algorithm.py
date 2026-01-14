# Python code for implementing MD5 Algorithm 
# MD5 is a hashing algorithm that produces a 128-bit fixed-length hash from any input.
import hashlib
# Imports Python’s built-in hashlib module, which provides many cryptographic hash functions like MD5, SHA-1, SHA-256, etc.

result = hashlib.md5(b'Ismile')
result1 = hashlib.md5(b'Esmile')
# hashlib.md5() creates a hash object for MD5.
# b'Ismile' → the b prefix converts the string into bytes, because MD5 works on byte data, not strings.

# printing the equivalent byte value
print("The byte equivalent of hash is : ", end="")
print(result.digest())
print("The byte equivalent of hash is : ", end="")
print(result1.digest())
# result.digest() → returns the hash as a bytes object (raw binary form, 16 bytes for MD5).
# end="" in print() ensures the next print appears on the same line.
# result1.digest() → returns the MD5 hash for "Esmile" in bytes.