# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:55:45 2022

@author: USER
"""
import socket
import sys

def optener_ip():
    hostname =  socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print("El nombre de tu ordenador es: "+ hostname)
    print("tu direccion IP es: "+ ip)

def portScaner():
    objetivo = socket.gethostbyname(input("Ingrese la direccion ID: "))
    print("Escaneando objetivo: " + objetivo)
    try:
        for port in range(1,150):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            resultado =s.connect_ex((objetivo,port))
            if resultado == 0:
                print("El puerto {} esta abierto".format(port))
            s.close()
    except:
        print(" ")
        print("Saliendo...")
        sys.exit(0)

def binario(decimal):
    binario = ""
    while decimal // 2 != 0 :
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal)+binario
def conver_binario():
    numero = int(input("Ingrese el numero que quiere convertir: "))
    print(binario(numero))
    

conver_binario()
  