from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


def keygen():
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048,backend=default_backend())
    
