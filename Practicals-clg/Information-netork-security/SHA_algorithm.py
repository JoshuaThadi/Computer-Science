# Python code for implementing SHA-256 based Digital Signature
# ! pip install pycryptodome

from Crypto.Signature import PKCS1_v1_5 # type: ignore
from Crypto.Hash import SHA256 # type: ignore
from Crypto.PublicKey import RSA # type: ignore
from Crypto import Random # type: ignore

# Function to generate a digital signature
def generate_signature(private_key, message):
    # Load the private key
    key = RSA.import_key(private_key)
    # Generate SHA-256 hash of the message
    hashed_message = SHA256.new(message.encode('utf-8'))
    # Create a signer using the private key
    signer = PKCS1_v1_5.new(key)
    # Generate the signature
    signature = signer.sign(hashed_message)
    return signature

# Function to verify a digital signature
def verify_signature(public_key, message, signature):
    # Load the public key
    key = RSA.import_key(public_key)
    # Generate SHA-256 hash of the message
    hashed_message = SHA256.new(message.encode('utf-8'))
    # Create a verifier using the public key
    verifier = PKCS1_v1_5.new(key)
    # Verify the signature (returns True if valid, False otherwise)
    return verifier.verify(hashed_message, signature)

# Generate RSA key pair
random_generator = Random.new().read
key_pair = RSA.generate(2048, random_generator)

# Extract public and private keys
public_key = key_pair.publickey().export_key()
private_key = key_pair.export_key()

# Example usage
message = "Hello, World!"

# Generate a digital signature
signature = generate_signature(private_key, message)
print("Generated Signature:", signature.hex())  # Show as hex string for readability

# Verify the digital signature
is_valid = verify_signature(public_key, message, signature)
print("Signature Verification Result:", is_valid)
