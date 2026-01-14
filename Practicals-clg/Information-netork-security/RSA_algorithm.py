# Python code for implementing RSA Algorithm
# Install library: pip install pycryptodome

# from Crypto.PublicKey import RSA # type: ignore
# from Crypto.Cipher import PKCS1_OAEP # type: ignore
# import binascii
# # RSA → Used to generate public and private keys.
# # PKCS1_OAEP → Secure padding scheme for RSA encryption/decryption.
# # binascii → Used to convert binary data into a readable hexadecimal format.

# # Generate RSA key pair (public + private)
# keyPair = RSA.generate(1024) # Generates a 1024-bit RSA key pair (private + public).

# # Get the public key
# pubKey = keyPair.publickey()
# print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")

# # Export public key in PEM format
# pubKeyPEM = pubKey.export_key() # export_key() exports keys in PEM format (readable).
# print(pubKeyPEM.decode('ascii'))

# # Display private key details
# print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")

# # Export private key in PEM format
# privKeyPEM = keyPair.export_key()
# print(privKeyPEM.decode('ascii'))

# # Encryption
# msg = "Ismile Academy".encode('utf-8')  # Convert string to bytes
# encryptor = PKCS1_OAEP.new(pubKey)
# encrypted = encryptor.encrypt(msg)
# print("Encrypted:", binascii.hexlify(encrypted).decode('ascii'))
# # Converts text message to bytes.
# # Creates an encryptor using the public key.
# # Encrypts the message.

# # Decryption (optional)
# decryptor = PKCS1_OAEP.new(keyPair)
# decrypted = decryptor.decrypt(encrypted)
# print("Decrypted:", decrypted.decode('utf-8'))
# Uses the private key to decrypt the ciphertext back into the original plaintext.

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate RSA key pair
keyPair = RSA.generate(1024)

# Get public key
pubKey = keyPair.public_key()
print(f"Public key: (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.export_key()
print(pubKeyPEM.decode('ascii'))

# Get private key
print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.export_key()
print(privKeyPEM.decode('ascii'))

# Encryption
msg = 'Ismile Academy'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg.encode('utf-8'))
print("Encrypted:", binascii.hexlify(encrypted))
