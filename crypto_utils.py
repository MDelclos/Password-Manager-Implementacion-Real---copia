import base64
from hashlib import scrypt
import json
from collections import namedtuple
import os
import bcrypt
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from auth import *

def derivar_clave_fernet(clave_maestra, salt):
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=base64.b64decode(salt.encode()), iterations=10_000)
    key = kdf.derive(clave_maestra.encode())
    return base64.urlsafe_b64encode(key)

def genera_hash_salt(clave_maestra_plana):
    hashClave = bcrypt.hashpw(clave_maestra_plana.encode(), bcrypt.gensalt()).decode("utf-8")
    salt = base64.b64encode(os.urandom(16)).decode("utf-8")
    return hashClave, salt

def desencripta_registros(username, clave_fernet):
    fernet = Fernet(clave_fernet)
    with open(f"users/{username}/vault.enc", "rb") as f:
        desencriptado = fernet.decrypt(f.read())
    return json.loads(desencriptado.decode())