import string
import random

#establece la longitud de la contraseña
longitud_pass = int(input("Ingrese el tamaño de la contraseña: "))

#genera una contraseña aleatoria
caracteres = string.ascii_letters + string.digits + string.punctuation

#genera aleatoriamente la contraseña con la longirtud esperada
contraseña = "".join (random.choice(caracteres) for i in range(longitud_pass))

#imprime la contraseña 
print("la contraseña generada es: " + contraseña) 