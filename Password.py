import itertools

# Esta línea abre n archivo de texto llamado "combinaciones.txt" en modo de escritura ("w" significa "write"). 
# Si el archivo no existe, se creará automáticamente. Si el archivo ya existe, se sobrescribirá con cualquier contenido anterior.
archivo = open("combinaciones2.txt", "w")

# Definir caracteres posibles
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@()[]{}*,:/-_¿?.¡$<#>&+%="

# Generar combinaciones de longitud 1, 2 y 3
# El bucle externo for recorre todas las longitudes de combinación posibles, desde 1 hasta 3 en este caso
for longitud in range(2, 3):
    #El bucle interno for utiliza la función product() de itertools para generar todas las posibles combinaciones de caracteres de la longitud actual. 
    for combinacion in itertools.product(caracteres, repeat=longitud):
        # Convertir la combinación en una cadena y escribirla en el archivo
        contrasena = "".join(combinacion)
        archivo.write(contrasena + "\n")

# Cerrar el archivo de texto
archivo.close() 