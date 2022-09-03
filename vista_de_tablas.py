# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 23:06:11 2022

@author: USER
"""
from tkinter import *
from tkinter import ttk
ventana = Tk()
ventana.title("Ejemplo de TreeView")
ventana.geometry("400x300")
ventana["bg"]="#fb0"
tv = ttk.Treeview(ventana)
item1 = tv.insert("",END,text="Dias")
horaL = tv.insert(item1,END,text="Lunes")
tv.insert(horaL,END,text="8:00 - 7:15")
tv.insert(item1,END,text="Martes")
tv.insert(item1,END,text="Miercoles")
tv.insert(item1,END,text="Jueves")
tv.insert(item1,END,text="Viernes")
tv.insert(item1,END,text="Sabado")
tv.insert(item1,END,text="Domingo")
item2 = tv.insert("", END,text="Meses" )
tv.insert(item2,END,text="Enero")
tv.pack()

ventana.mainloop()