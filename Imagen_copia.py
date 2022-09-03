# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 23:31:54 2022

@author: USER
"""
import cv2
import random
import turtle

def version():
    print("La vesion es: ")
    print(cv2.__version__)
def alee():
    hola = random.sample(range(100),50)
    hol = ["Hola", "Como", "Estas"]
    print(random.choice(hol))
    print(hola)
# valor = random.sample(range(50),2)
def imagenCopia():
    try:
        #espicificar la ruta de la imagen
        im1 = cv2.imread(r'C:\Users\USER\Desktop\bebe.jpg')
        window_name = 'Original imagen'
        #mostrar la imagen original
        cv2.imshow(window_name, im1)
        #Convertir los colores
        grey_img = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
        invertir = 255-grey_img
        #imagen
        blur = cv2.GaussianBlur(invertir,(21,21),0)
        invertedblur = 255-blur
        sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
        #Guardar la imagen
        cv2.imwrite(r"C:\Users\USER\Desktop\copia2.jpg", sketch)
        imagen2 = cv2.imread(r"C:\Users\USER\Desktop\copia2.jpg")
        window_name = 'Copia imagen'
        cv2.imshow(window_name, imagen2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except (ValueError):
        print(ValueError)

def reloj():
    try:
        
        s=turtle.Screen()
        t=turtle.Turtle()
        s.setup(620.620)
        s.bgcolor('black')
        t.pensize(4)
        t.shape('turtle')
        t.penup()
        t.pencolor('cyan')
        m=0
        for i in range(12):
            m = m+1
            t.penup()
            t.setheading(-30*i+60)
            t.forward(150)
            t.pendown()
            t.forward(25)
            t.penup()
            t.forward(20)
            t.write(str(m),align="center", font=("Arial", 12, "normal"))
            if m==12:
                m=0
            t.home()
        t.home()
        t.setpos(0,-250)
        t.pendown()
        t.pensize(10)
        t.pencolor('yellow')
        t.circle(250)
        t.penup()
        t.setpos(0,-290)
        t.pendown()
        t.pencolor('red')
    
        t.hideturtle()
    except(Exception) :
        print(Exception)
imagenCopia()
