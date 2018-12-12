import utils
import datetime

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes


'''
https://cryptography.io/en/latest/x509/tutorial/
'''


def keygen():
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048,backend=default_backend())

    sk = key.private_bytes(encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                        encryption_algorithm=serialization.BestAvailableEncryption(b"passphrase")

'''
Information required in certificate (for both subjects and issuers)
'''
def cert_info(name, email, country, state, city, org_name):
    name = name.encode("utf-8")
    email = email.encode("utf-8")
    country = country.encode("utf-8")
    state = state.encode("utf-8")
    city = city.encode("utf-8")
    org_name = org_name.encode("utf-8")

    info = x509.Name([
        # Provide various details about who we are.
        x509.NameAttribute(NameOID.COUNTRY_NAME, country),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state),
        x509.NameAttribute(NameOID.LOCALITY_NAME, city),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, org_name),
        x509.NameAttribute(NameOID.COMMON_NAME, name),
        x509.NameAttribute(NameOID.EMAIL_ADDRESS, email)
        ])
    return info

'''
Generate a Certificate Signing Request (CSR)
'''
def CSRgen(passphrase, name, email, country, state, city, org_name, filename='csr.pem'):
    subject = cert_info(name, email, country, state, city, org_name)

    csr = x509.CertificateBuilder().subject_name(
        subject
        # Sign the CSR with our private key.
        ).sign(key, hashes.SHA256(), default_backend())

    # Write our CSR out to disk.
    with open(filename, "wb") as f:
        f.write(csr.public_bytes(serialization.Encoding.PEM))


'''
Generate a self-signed Certificate
'''
def self_sign_gen(issuer, pk, filename):
    cert_gen(issuer, issuer, pk, filename)


'''
Generate a Certificate
'''
def cert_gen(subject, issuer, pk, filename='certificate.pem'):
    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        pk
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        # Our certificate will be valid for 10 days
        datetime.datetime.utcnow() + datetime.timedelta(days=10)
    )
    # Sign our certificate with our private key
    ).sign(key, hashes.SHA256(), default_backend())

    # Write our certificate out to disk.
    with open(filename, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))


def hash(x):
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(x)
    return digest.finalize()


def dhash(x):
    return hash(hash(x))


def sign_entry(text, pk):
    pass
