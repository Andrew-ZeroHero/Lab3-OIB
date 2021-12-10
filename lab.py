import os
import pickle
import json
import argparse
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

key = os.urandom(32)
nonce = os.urandom(16)
print(type(key))
print(key)
print(nonce)
file_name = 'symmetric_key.txt'
with open(file_name, 'wb') as key_file:
  key_file.write(key)
 
file_name = 'symmetric_nonce.txt'
with open(file_name, 'wb') as nonce_file:
  nonce_file.write(nonce)

txt_file = '/content/text.txt'
with open(txt_file, 'rb') as read_file:
  text = read_file.read()
algorithm = algorithms.ChaCha20(key, nonce)
cipher = Cipher(algorithm, mode=None)
encryptor = cipher.encryptor()
enc_txt = encryptor.update(text)

print(enc_txt)
decryptor = cipher.decryptor()
decryptor.update(enc_txt)
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

keys = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
private_key = keys
public_key = keys.public_key()

print(type(private_key))
print(private_key)
print(type(public_key))
print(public_key)
