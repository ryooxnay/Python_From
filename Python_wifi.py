# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:59:59 20022

@author: USER
"""
#re para expeciones regulares

import subprocess
import re

def clavesAntiguasWifi():
    command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
    print(command_output)
    commando = subprocess.run(["netsh ", "wlan ", "show ", "profiles ", "Taller ", "key" "=" "clear"],capture_output=True).stdout.decode()
    print(commando)
    profile_names=(re.findall("Perfiles de usuario: (.*)\r", command_output))
    print(profile_names)
    wifi_list=[]
    if len(profile_names) != 0:
        for name in profile_names:
            wifi_profile = {}
            profile_info=subprocess.run(["netsh", "wlan", "show", "profiles",name],capture_output = True).stdout.decode()
            if re.search("Security key      : Absent", profile_info):
                print(profile_info)
                continue
            else:
                wifi_profile["ssid"]=name
                profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profiles",name,"key=clear"],capture_output=True).stdout.decode()
                password = re.search("Key Content: (.*)\r",profile_info_pass )
                if password == None:
                    wifi_profile["password"]=None
                else:
                    wifi_profile["password"]=password[1]
                
                wifi_list.append(wifi_profile)
    for x in range(len(wifi_list)):
        print(wifi_list[x])
            
    
def limpiarDatos():
    command_output = subprocess.run(["fsutil","fsinfo","drives"], capture_output=True).stdout.decode()
    print(command_output)
    print("No puedes limpiar los datos de la unida C:\ ")
    unidad = input("Ingrese la unidad que quiere limpiar : ")
    command_output = subprocess.run([unidad])
    command_output = subprocess.run(["attrib", "/d", "/s", "-r", "-h", "-s", "*.*"], capture_output=True).stdout.decode()
    
def limpiarRam():
    print("hola")

limpiarDatos()     
            
            
            
            
            
            
            
            
            
            
            
            