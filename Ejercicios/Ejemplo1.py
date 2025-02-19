login_success = ["success", "success", "fail", "success"]
datas_type = type(login_success)
print(datas_type)

#Habra alguna afectacion si agrego otro codigo ?
failed_at = 3
failed_at = 4
print(failed_at)

dan = "5.2" 
da_1 =type(dan)
print(da_1)

#tipo de datos tupla entre parentesis
cadena = ("Ana", "Belen")
data_type=type(cadena)
print(data_type)

#lista, entre corchetes
diccionario = ["hola", "Ana","Belen", 12, True]
data_types=type(diccionario)
print(data_types)
print(diccionario)

#Viene diccionario, entre llaves, 
diccionarioR = {1:"ruca", 2: "Bruja maldita", 3:"Pioja"}
datas_type2= type(diccionarioR)
print(datas_type2)
print(diccionarioR)

#conjunto, valores unicos, sin un orden especifico : sin valores repetidos. al imprimir los valores se mantienen sin un orden especifico. 
conjunto ={"Ana", "Belen", "simpatica", "AnaBelen"}
data_types3 = type(conjunto)
print(data_types3) 
print(conjunto)

#Reasigancion
devide_id = "asdasdawe"
print(devide_id)
devide_id = "fghdfgdfgdf"
print(devide_id)

#Reasignacion caso 2: 
username = "hgfghfg"
old_username = username
username = "lollolol"
print("Usuario previo: ", old_username)
print("Usuario actual: ", username)

#lista
# Asigna `lista_usuarios` a la lista de nombres de usuario a los que se les permite acceder al dispositivo

lista_usuarios = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"] 

# Muestra `lista_usuarios`

print(lista_usuarios)

## Asigna `lista_usuarios` a la lista de nombres de usuario a los que se les permite acceder al dispositivo
lista_usuarios = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]
# Asigna `tipo_lista_usuarios` al tipo de dato de `lista_usuarios`
tipo_lista_usuarios =type(lista_usuarios)
# Muestra `tipo_lista_usuarios`
print(tipo_lista_usuarios)

# reasignar
# Asigna `lista_usuarios` a la lista de nombres de usuario a los que se les permite acceder al dispositivo
lista_usuarios = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]
# Muestra `lista_usuarios`
print(lista_usuarios)
# Asigna a `lista_usuarios` la lista actualizada de nombres de usuario a los que se les permite acceder al dispositivo
lista_usuarios = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards", "lpope"]
# Muestra `lista_usuarios`
print(lista_usuarios)


# Asigna a `max_inicios_sesion` el valor 3
max_inicios_sesion = 3
# Asigna `intentos_inicio_sesion` al valor 2
intentos_inicio_sesion = 2
# Determina si el número actual de intentos de inicio de sesión que realizó un usuario es menor o igual al número máximo de intentos de inicio de sesión permitidos,
# y muestra el valor booleano resultante
print(intentos_inicio_sesion <= max_inicios_sesion)
    
#Condiciones
operating_system = "OS 3"
# Comprueba si el sistema operativo es "OS 2" y muestra el valor boolean
if operating_system == "OS 2":
    print("El sistema operativo es OS 2") 
else: 
    print("El sistema operativo no es OS 2, por lo tanto debe realizarse una actualizacion")


#Comprobar la version de sistema operativo
# Asigna una variable llamada `system` a un sistema operativo específico, representado como una cadena
# Esta variable indica qué sistema operativo se está ejecutando
# No dudes en ejecutar esta celda varias veces; cada vez prueba asignar a `system` diferentes valores ("OS 1", "OS 2", "OS 3") y observa el resultado

system = "OS 3"
# Si se está ejecutando OS 2, muestra un mensaje de "no es necesario actualizar"
if (system == "OS 2"):
    print("no es necesario actualizar")
else:
    print("Debes actualizar perro")

########################
# Asigna a `system` un sistema operativo específico
# Esta variable representa el sistema operativo que se está ejecutando

system = "OS 4"

# Si se está ejecutando OS 2, muestra un mensaje de "no es necesario actualizar"
# En caso contrario, si se está ejecutando OS 1, muestra un mensaje de “es necesario actualizar”
# En caso contrario, si se está ejecutando OS 3, muestra un mensaje de “es necesario actualizar”

if system == "OS 2":
    print("no es necesario actualizar")
elif system == "OS 1":
    print("es necesario actualizar")
elif system == "OS 3":
    print("es necesario actualizar")
else:
    print("Es otra version instalada perro")

#####
# Asigna `approved_user1` y `approved_user2` a los nombres de usuario de los usuarios autorizados

approved_user1 = "elarson"
approved_user2 = "bmoreno"

# Asigna `username` al nombre de usuario de un usuario específico que intenta iniciar sesión

username = "bmoreno"

# Si el usuario que intenta iniciar sesión se encuentra entre los usuarios autorizados, se mostrará un mensaje indicando que está autorizado para acceder a este dispositivo
# En caso contrario, se mostrará un mensaje indicando que no tiene acceso a este dispositivo

if approved_user1 == "elarson" and approved_user2 == "bmoreno":
    print("Este usuario tiene acceso a este dispositivo.")
elif username == "elarson": 
    print("Este usuario no tiene acceso a este dispositivo.")
else:
    print("Este usuario no tiene acceso a este dispositivo.")

##############
# Asigna `approved_list` a una lista de nombres de usuario autorizados

approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Asigna `username` al nombre de usuario de un usuario específico que intenta iniciar sesión

username = "bmoreno"

# Asigna `organization_hours` a un valor booleano que represente si el usuario intenta iniciar sesión durante el horario de la organización

organization_hours = True

# Si el usuario se encuentra entre los usuarios autorizados y está iniciando sesión durante el horario de la organización, comunica que el usuario ha iniciado sesión
# En caso contrario, comunica que el nombre de usuario no está autorizado o que el intento de inicio de sesión se realizó fuera del horario de la organización

if username in approved_list and organization_hours == True:
    print("Intento de inicio de sesión realizado por un usuario autorizado durante el horario de la organización.")
else:
    print("Nombre de usuario no autorizado o intento de inicio de sesión realizado fuera del horario de la organización.")



#############
##genera una lista de postres los cuales seran evaluados y entregados en tiempo y forma, si por ejemplo el horario aun es en el dia, 
##entonces se puede entregar en tiempo y forma, si no, entonces no se puede entregar

print("\n")
postres_variados = ["Flan", "Pastel", "Tarta de nuez", "Gelatina de Chocolate", "Cheesecake", "Helado"]

postre_en_servicio = "Tarta de nuez"

horario_vespertino = True

if postre_en_servicio in postres_variados and horario_vespertino == True : 
    print("Excelente, su peticion puede ser enviada en tiempo y forma, gracias por su conmfianza")
else:
    print("No se puede entregar en tiempo y forma")


####
print("\n")
# Asigna `postres_variados` a una lista de postres disponible
for i in["Flan", "Pastel", "Tarta de nuez", "Gelatina de Chocolate", "Cheesecake", "Helado"]:
    print(f'El postre {i} disponible para poder pedirlo a domicilio') 
    