import json
import os
from auth import *
from crypto_utils import *
from cryptography.fernet import Fernet

def crea_carpeta_nueva(username, clave_maestra_plana, salt):
    os.makedirs(f"users/{username}", exist_ok=True)
    vacio = {}
    contenido_bytes = json.dumps(vacio).encode()
    contenido_cifrado = Fernet(derivar_clave_fernet(clave_maestra_plana, salt)).encrypt(contenido_bytes)
    with open(f"users/{username}/vault.enc", "wb") as f:
        f.write(contenido_cifrado)

def ingresa_usuario_index(username, hashClave, salt, ruta_json):
    try:
        if os.path.getsize(ruta_json) == 0:
            diccionario = {}
        else:
            with open(ruta_json, "r", encoding="utf-8") as f:
                diccionario = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        diccionario = {}

    with open(ruta_json, "w", encoding="utf-8") as f:
        diccionario[username] = {"clave_maestra_hash":hashClave, "salt":salt}
        json.dump(diccionario, f, indent=2)

def guarda_registro(registros, username, clave):
    contenido_bytes = json.dumps(registros).encode()
    contenido_cifrado = Fernet(clave).encrypt(contenido_bytes)
    print(registros)
    print(contenido_cifrado)
    with open(f"users/{username}/vault.enc", "wb") as f:
        f.write(contenido_cifrado)