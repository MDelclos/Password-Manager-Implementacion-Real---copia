
import tkinter as tk

from auth import *
# pantalla_inicio will be imported inside boton_volver to avoid circular imports

def boton_exit(ventana):
    exit_button = tk.Button(ventana, text="Salir", font=15, command=lambda: ventana.destroy())
    exit_button.place(x=170, y=260)

def boton_volver(ventana):
    from gui_screens import pantalla_inicio
    volver = tk.Button(ventana, text="Volver", font=15, command=lambda: (ventana.destroy(), pantalla_inicio()))
    volver.place(x=290, y=260)

def crea_ventana(titulo):
    ventana = tk.Tk()
    ventana.title(titulo)
    ventana.geometry("400x300")
    boton_exit(ventana)
    return ventana