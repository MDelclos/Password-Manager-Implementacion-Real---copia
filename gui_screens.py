import tkinter as tk

from auth import *

from gui_utils import *
from vault_manager import guarda_registro


def pantalla_inicio():
    ventana = crea_ventana("Password Manager Login")

    label_inicio = tk.Label(ventana,
                            text="Pulse el botón adecuado para continuar",
                            font=("Arial", 15))
    label_inicio.pack(pady=20)

    boton_inicia_sesion = tk.Button(ventana,
                                    text="Iniciar sesión", 
                                    font=("Arial", 12),
                                    command=lambda: pantalla_inicia_sesion(ventana))
    boton_inicia_sesion.pack(pady=5)

    boton_registra_usuario = tk.Button(ventana, 
                                       text="Nuevo usuario", 
                                       font=("Arial", 12),
                                       command=lambda: pantalla_registro_usuario(ventana))
    boton_registra_usuario.pack(pady=5)

    ventana.mainloop()

def pantalla_inicia_sesion(ventana_anterior):
    ventana_anterior.destroy()
    ventana = crea_ventana("Inicia Sesión")
    
    label_inicio = tk.Label(ventana,
                            text="Ingrese su usuario y su contraseña",
                            font=("Arial", 15),
                            wraplength=350, 
                            justify="center")
    label_inicio.pack(pady=20)

    entry_usuario = tk.Entry(ventana,
                             font=("Arial", 12))
    entry_usuario.pack(pady=5)

    entry_contrasenya = tk.Entry(ventana,
                             font=("Arial", 12),
                             show="*")
    entry_contrasenya.pack(pady=5)

    mensaje = tk.Label(ventana, text="", font=("Arial", 12))
    mensaje.pack(pady=5)

    def handle_login():
        if entry_contrasenya.get().strip() == "" or entry_usuario.get().strip() == "":
            mensaje.config(fg="red", text="Los campos no pueden estar vacios.")
        else:
            res, boolean = iniciar_sesion(entry_usuario.get(), entry_contrasenya.get())
            if boolean:
                mensaje.config(fg="green", text="Inicio de sesion exitoso. Entrando en 3...")
                pantalla_sesion_iniciada(ventana, entry_usuario.get(), res)
            else:
                mensaje.config(fg="red", text=res)


    boton_enter = tk.Button(ventana,
                            text="Enter",
                            font=("Arial", 12),
                            command=handle_login)
    boton_enter.pack(pady=5)

    boton_volver(ventana)


def pantalla_registro_usuario(ventana_anterior):
    ventana_anterior.destroy()
    ventana = crea_ventana("Registra Usuario")

    label_registro = tk.Label(ventana,
                              text="Ingrese el nombre de usuario y su contraseña deseada",
                              font=("Arial", 15),
                              wraplength=350, 
                              justify="center")
    label_registro.pack(pady=20)

    entry_usuario = tk.Entry(ventana,
                             font=("Arial", 12))
    entry_usuario.pack(pady=5)

    entry_contrasenya = tk.Entry(ventana,
                             font=("Arial", 12),
                             show="*")
    entry_contrasenya.pack(pady=5)

    mensaje = tk.Label(ventana, text="", font=("Arial", 12))
    mensaje.pack(pady=5)

    def handle_register():
        if entry_usuario.get().strip() == "" or entry_contrasenya.get().strip() == "":
            mensaje.config(fg="red", text="Los campos no pueden estar vacios.")
        else:
            boolean = cargar_nuevo_usuario(entry_usuario.get(), entry_contrasenya.get())
            if boolean:
                mensaje.config(fg="green", text="Nuevo usuario creado.")
            else:
                mensaje.config(fg="red", text="El usuario ya existe.")

    boton_enter = tk.Button(ventana,
                            text="Enter",
                            font=("Arial", 12),
                            command=handle_register)
    boton_enter.pack(pady=5)

    boton_volver(ventana)

def pantalla_sesion_iniciada(ventana_anterior, username, clave):
    ventana_anterior.destroy()
    ventana = crea_ventana("Sesion iniciada")
    boton_exit(ventana)
    boton_volver(ventana)

    registros = desencripta_registros(username, clave)
    print(registros)

    label_bienvenida = tk.Label(ventana,
                                text=f"Bienvenido/a {username}",
                                font=("Arial", 15),
                                wraplength=350, 
                                justify="center")
    label_bienvenida.pack(pady=20)

    button_nuevo_ingreso = tk.Button(ventana,
                                     text="Nuevo registro",
                                     font=("Arial", 12),
                                     command=lambda: (handle_nuevo_reg(registros)))
    button_nuevo_ingreso.pack(pady=5, padx=20)

    button_eliminar_registro = tk.Button(ventana,
                                     text="Elimina registro",
                                     font=("Arial", 12),
                                     command=lambda: print("elimina_registro()"))
    button_eliminar_registro.pack(pady=5, padx=2)

    button_busca_registro = tk.Button(ventana,
                                     text="Busca registro",
                                     font=("Arial", 12),
                                     command=lambda: print("busca_registro()"))
    button_busca_registro.pack(pady=5, padx=2)

    button_todos_registros = tk.Button(ventana,
                                     text="Todos los registros",
                                     font=("Arial", 12),
                                     command=lambda: print("todos_registros()"))
    button_todos_registros.pack(pady=5, padx=2)

    button_todos_registros = tk.Button(ventana,
                                     text="Guardar cambios",
                                     command=lambda: guarda_registro(registros, username, clave))
    button_todos_registros.pack(pady=5, padx=2)

    def handle_nuevo_reg(registros):
        nuevo_registro = pantalla_nuevo_registro(registros)
        if not (len(registros) >= len(nuevo_registro)):
            registros = nuevo_registro

def pantalla_nuevo_registro(registros):
    ventana = tk.Toplevel()
    ventana.title("Nuevo Registro")
    ventana.geometry("350x300")

    tk.Label(ventana, text="Nombre registro")
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    tk.Label(ventana, text="Servicio:").pack()
    entry_servicio = tk.Entry(ventana)
    entry_servicio.pack()

    tk.Label(ventana, text="Contraseña:").pack()
    entry_contrasenya = tk.Entry(ventana)
    entry_contrasenya.pack()

    tk.Label(ventana, text="Usuario/Correo:").pack()
    entry_usuario = tk.Entry(ventana)
    entry_usuario.pack()

    opciones = ["Redes sociales", "Juegos", "Educacion", "Suscripciones", "Otros"]
    seleccion = tk.StringVar(value=opciones[0])
    tk.Label(ventana, text="Tipo de servicio:").pack()
    menu_tipo = tk.OptionMenu(ventana, seleccion, *opciones)
    menu_tipo.pack()

    def ingresa():
        registros[entry_nombre.get().strip()] = {"Servicio":entry_servicio.get().strip(),
                                                "Contrasenya":entry_contrasenya.get().strip(),
                                                "Usuario":entry_usuario.get().strip(),
                                                "Tipo":seleccion.get().strip()}
        
    tk.Button(ventana,
              text="Guardar",
              command=ingresa).pack()
    ventana.wait_window()

    return registros
