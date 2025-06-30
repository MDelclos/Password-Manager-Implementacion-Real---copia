import json
import bcrypt

from crypto_utils import *
from vault_manager import *

ruta_json = r"C:\Users\delcl\Documents\Proyectos ciber\Password Manager Implementacion Real\users\index.json"

def cargar_usuarios():
    try:
        with open(ruta_json, "r", encoding="utf-8") as f:
            datos = json.load(f)
            return datos
    except json.JSONDecodeError:
        return {}
 
def cargar_nuevo_usuario(username, clave_maestra_plana):

    if check_usuario_existe(username):
        return False
    else:
        hashClave, salt = genera_hash_salt(clave_maestra_plana)

        ingresa_usuario_index(username, hashClave, salt, ruta_json)

        crea_carpeta_nueva(username, clave_maestra_plana, salt)
        
        return True

def check_usuario_existe(username):
    usuarios = cargar_usuarios()
    if username in usuarios:
        return True
    return False

def iniciar_sesion(username, clave_maestra):
    if username.strip() == "" or clave_maestra.strip() == "":
        return "Los campos no pueden estar vacios.", False
    usuarios = cargar_usuarios()
    if check_usuario_existe(username):
        if bcrypt.checkpw(clave_maestra.encode(), usuarios[username]["clave_maestra_hash"].encode()):
            clave_fernet = derivar_clave_fernet(clave_maestra, usuarios[username]["salt"])
            return clave_fernet, True
        else:
            return "La clave maestra es erronea.", False
    return "El usuario no existe.", False
