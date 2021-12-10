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

with open('settings.json') as json_file:
    json_data = json.load(json_file)

initial_path = json_data["initial_file"]
encrypted_path = json_data["encrypted_file"]
decrypted_path = json_data["decrypted_file"]
symmetric_path = json_data["symmetric_key"]
public_path = json_data["public_key"]
secret_path = json_data["secret_key"]

def key_generation(path_to_symmetric_key: str, path_to_public_key: str, path_to_secret_key: str) -> None:

# Переделать!
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
