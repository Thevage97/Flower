import tkinter as tk
import turtle
from turtle import *
import colorsys

def ejecutar_script_turtle():
    # Creamos una ventana de turtle
    ventana_turtle = turtle.Screen()
    ventana_turtle.setup(width=1.0, height=1.0)  # Configuramos la ventana para que se muestre en pantalla completa
    ventana_turtle._root.overrideredirect(True)  # Eliminamos los bordes y la barra de título de la ventana

    # Ejecutamos el script de turtle
    tracer(100)
    h = 0.85
    speed(25)
    bgcolor("black")

    for i in range(190):
        c = colorsys.hsv_to_rgb(h,1,1)
        fillcolor(c)
        h += 0.0015
        begin_fill()
        circle(190-i, 90)
        lt(75)
        lt(20)
        circle(190-i, 90)
        lt(18)
        end_fill()

    done()

# Creamos una ventana principal
ventana = tk.Tk()
ventana.title("Mi botón")

# Creamos un botón con fondo negro y texto blanco
boton = tk.Button(ventana, text="Click aquí", bg="black", fg="white", command=ejecutar_script_turtle)

# Agregamos el botón a la ventana
boton.pack()

# Iniciamos la ventana
ventana.mainloop()