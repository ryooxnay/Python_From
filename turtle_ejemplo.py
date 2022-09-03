# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 19:57:30 2022

@author: USER
"""
#'' % \
from turtle import *
import random
"""
shape(f):       Cambia la forma del cursor. f puede ser "arrow", "turtle", "circle", "square", "triangle" o "classic".
forward(d):     Mueve el cursor hacia delante la distancia d.
backward(d):    Mueve el cursor hacia atrás la distancia d.
right(a):       Gira el cursor hacia la derecha a grados.
left(a):        Gira el cursor hacia la izquierda a grados.
goto(x,y):      Mueve al cursor a la posición x y y.
up():           Levanta el lápiz de dibujo, si el lápiz está levantado el cursor no dibujará cuando se mueva.
down():         Baja el lápiz de dibujo, por defecto el lápiz estará bajado. Cuando el lápiz está bajado y movamos el cursor, se dibujará el recorrido.
color(c):       Cambiamos el color con el que el cursor pintará al color c.
dot():          Dibuja un punto en la posición donde está el cursor.
fillcolor(c):   Cambia el color de relleno de polígonos al color f.
begin_fill():   Marca el punto inicial para rellenar un polígono de color.
end_fill():     Marca el punto final para rellenar un polígono con color.
circle(r,g):    Dibuja un círculo de radio r, si se indica g dibujará g grados del círculo, si no se indica nada dibujará el círculo entero.
pensize(w):     Cambia el grosor del lápiz a w puntos.
"""
title("Jugando")
#bgcolor('black')
setup(800,600,250,75)

def Tringulo():
    """ Triangulo"""
    up()
    goto(0,0)
    down()
    color("red")
    goto(300,0)
    goto(150,150)
    goto(0,0)
    up()
    goto(350,0)
    color("black")
    write("#1 Triangulo ",False ,"center")
    
def Cuadrado():
    """  Cuadrado """
    up()
    goto(-350,-150)
    down()
    color("blue")
    begin_fill()
    fillcolor("blue")
    goto(-50,-150)
    goto(-50,150)
    goto(-350,150)
    goto(-350,-150)
    end_fill()
    up()
    color("black")
    goto(-320,-170)
    write("#2 Cuadrado ", False, "center")

def Circulo():
    """ Circulo  """
    begin_fill()
    fillcolor("black")
    circle(100)
    end_fill()
    write("#3 Circulo ", false, "center")
def aros():
    color("yellow")
    begin_fill()
    fillcolor("yellow")
    circle(150)
    end_fill()
    color("gray")
    begin_fill()
    fillcolor("gray")
    left(90)
    circle(150)
    end_fill()
    color("pink")
    begin_fill()
    fillcolor("pink")
    left(90)
    circle(150)
    end_fill()
    color("black")
    begin_fill()
    fillcolor("black")
    left(90)
    circle(150)
    end_fill()
    #
    color("red")
    begin_fill()
    fillcolor("red")
    circle(100)
    end_fill()
    color("blue")
    begin_fill()
    fillcolor("blue")
    left(90)
    circle(100)
    end_fill()
    color("green")
    begin_fill()
    fillcolor("green")
    left(90)
    circle(100)
    end_fill()
    color("orange")
    begin_fill()
    fillcolor("orange")
    left(90)
    circle(100)
    end_fill()
    # 1
    color("yellow")
    begin_fill()
    fillcolor("yellow")
    circle(50)
    end_fill()
    color("gray")
    begin_fill()
    fillcolor("gray")
    left(90)
    circle(50)
    end_fill()
    color("white")
    begin_fill()
    fillcolor("white")
    left(90)
    circle(50)
    end_fill()
    color("black")
    begin_fill()
    fillcolor("black")
    left(90)
    circle(50)
    end_fill()
    #
    color("red")
    begin_fill()
    fillcolor("red")
    circle(25)
    end_fill()
    color("blue")
    begin_fill()
    fillcolor("blue")
    left(90)
    circle(25)
    end_fill()
    color("green")
    begin_fill()
    fillcolor("green")
    left(90)
    circle(25)
    end_fill()
    color("orange")
    begin_fill()
    fillcolor("orange")
    left(90)
    circle(25)
    end_fill()
    
def entradaText():
    """
    título: el título de la ventana emergente.
    mensaje: el texto que se muestra en la ventana.
    """
    nombre = textinput("Nombre","Ingresa tu nombre.")
    
    """
    título: el título de la ventana emergente.
    mensaje: el texto que se muestra en la ventana.
    valorPredeterminado: el valor que se muestra en la ventana de forma predeterminada.
    valorMínimo: el valor mínimo que puede escribir el usuario.
    valorMáximo: el valor máximo que puede escribir el usuario.
    """
    edad = numinput("Edad", "Cual es tu edad", 28, 18, 80)
    color("black")
    goto(-350,0)
    write("Hola "+ nombre+ " tu edad es de "+ str(edad)+ " años")
def jugando():
    forward(100) # camina hacia el eje ++
    right(90) # gira a la derecha 90 grados
    forward(100)
    left(90) # gira a la izquierda 90 grados
    forward(100)
    backward(50) #regresa 50 px por donde venias
    right(90)
    forward(100)


def ondas():
    bgcolor('black')
    speed(0)
    x=1
    while x < 600:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colormode(255)
        pencolor(r,g,b)
        pensize(5)
        forward(5+x)
        right(91)
        x+=1
def estrella():
    bgcolor('black')
    speed(0)
    x=1
    while x < 600:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colormode(255)
        pencolor(r,g,b)
        pensize(5)
        forward(5+x)
        right(200)
        x+=1
estrella()
mainloop()

