

#    Import subprocess so we can use system commands.
import subprocess

#    Import the re module so we can make use of regular expressions. 
import re
# Python nos permite ejecutar comandos del sistema usando la función
# proporcionado por el módulo de subproceso;
# (subprocess.run(<la lista de argumentos de la línea de comando va aquí>, <especifique el segundo argumento si desea capturar la salida>)).
#
# Este script es un proceso principal que crea un proceso secundario que
# ejecuta un comando del sistema y solo continuará una vez que el proceso secundario
#    esta completado.
#
# Para guardar los contenidos que se envían al flujo de salida estándar
# (la terminal), primero debemos especificar que queremos capturar la salida.
# Para hacer esto especificamos el segundo argumento como capture_output = True.
# Esta información se almacena en el atributo stdout como bytes y
# debe decodificarse antes de usarse como una cadena en Python.
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
# Importamos el módulo re para hacer uso de expresiones regulares.
# Queremos encontrar todos los nombres wifi que se enumeran después
# "TODOS los perfiles de usuario:". Usando expresiones regulares podemos crear
# un grupo de todos los caracteres hasta que aparezca la secuencia de escape de retorno (\r).
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

#    We create an empty list outside of the loop where dictionaries 
#    containing all the wifi usernames and passwords will be saved.
wifi_list = []

#    If any profile names are not found this means that wifi connections 
#    have also not been found. So we run this part to check the 
#    details of the wifi and see whether we can get their passwords.
if len(profile_names) != 0:
    for name in profile_names:
        #    Every wifi connection will need its own dictionary which 
        #    will be appended to the variable wifi_list.
        wifi_profile = {}
        #    We can now run a more specific command to see the information 
        #    about the wifi connection and if the Security key
        #    is not absent it may be possible to get the password.
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], apture_output = True).stdout.decode()
        #    We use the regular expression to only look for the absent cases so we can ignore them.
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            #    Assign the ssid of the wifi profile to the dictionary.
            wifi_profile["ssid"] = name
            #    These cases aren't absent and we should run the 
            #    "key=clear" command part to get the password.
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key = clear"], capture_output = True).stdout.decode()
            #    Again run the regular expression to capture the 
            #    group after the : (which is the password).
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
            #    Check if we found a password using the regular expression. 
            #    Some wifi connections may not have passwords.
            if password == None:
                wifi_profile["password"] = None
            else:
                #    We assign the grouping (where the password is contained) that 
                #    we are interested in to the password key in the dictionary.
                wifi_profile["password"] = password[1]
            #    We append the wifi information to the variable wifi_list.
            wifi_list.append(wifi_profile) 

for x in range(len(wifi_list)):
    print(wifi_list[x])

