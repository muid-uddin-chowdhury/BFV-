import numpy as np

# Function to perform modular reduction
def mod(a, n):
    return a % n

# Function to generate keys
def keygen(poly_mod_degree, plain_mod):
    # Generate public and private keys for a simplified version
    secret_key = np.random.randint(1, plain_mod)
    public_key = np.random.randint(1, plain_mod, poly_mod_degree)
    
    return public_key, secret_key

# Function to encode plaintext as a polynomial
def encode(plain, poly_mod_degree):
    # Encodes the plaintext as a polynomial (here simplified)
    return [int(x) for x in bin(plain)[2:].zfill(poly_mod_degree)]

# Function to encrypt a plaintext using the public key
def encrypt(plain_poly, public_key, poly_mod_degree, plain_mod):
    noise = np.random.randint(1, plain_mod, poly_mod_degree)
    cipher = [(plain_poly[i] + public_key[i] + noise[i]) % plain_mod for i in range(poly_mod_degree)]
    
    return cipher

# Function to decrypt the ciphertext using the secret key
def decrypt(cipher, secret_key, plain_mod):
    plain_poly = [(cipher[i] - secret_key) % plain_mod for i in range(len(cipher))]
    
    # Convert back from polynomial to integer (simplified decoding)
    plain = sum([bit * (2 ** i) for i, bit in enumerate(plain_poly)])
    
    return plain

# Parameters
poly_mod_degree = 8  # Degree of the polynomial (simplified small degree)
plain_mod = 257      # Plaintext modulus (a prime number for modular arithmetic)

# Key generation
public_key, secret_key = keygen(poly_mod_degree, plain_mod)

# Message to encrypt
message = 42  # Example plaintext message (integer)

# Encode the message as a polynomial
plain_poly = encode(message, poly_mod_degree)
print(f"Encoded plaintext (as polynomial): {plain_poly}")

# Encrypt the encoded message
cipher = encrypt(plain_poly, public_key, poly_mod_degree, plain_mod)
print(f"Ciphertext: {cipher}")

# Decrypt the ciphertext back to the original message
decrypted_message = decrypt(cipher, secret_key, plain_mod)
print(f"Decrypted message: {decrypted_message}")
