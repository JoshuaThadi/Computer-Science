# Python code for implementing SHA Algorithm
# SHA-1 is a cryptographic hash function that produces a 160-bit (20-byte) fixed-length hash.
import hashlib
str = input("Enter the value of encode: ")
result = hashlib.sha1(str.encode())
# str.encode() → converts the string into bytes.
# Hash functions work on bytes, not plain strings.
# Example: "Hello".encode() → b'Hello'
# hashlib.sha1(...) → creates a SHA-1 hash object of the input bytes.
# This object stores the hash result internally.

print("The hexadecimal equivalent if SHA1 is: ")
print(result.hexdigest())
# result.hexdigest() → returns the SHA-1 hash as a readable hexadecimal string (instead of raw bytes).
# print() displays the hash value.