import sys 
import socket 

objetivo = socket.gethostbyname(input("Inserte la direccion IP: "))

print("Escaneando el objetivo: " + objetivo)

try: 
    for puerto in range(1, 1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resultado = s.connect_ex((objetivo, puerto))
        if resultado == 0:
            print("Puerto {} abierto".format(puerto))
            s.close()
except:
    print("Error en el escaneo")
    sys.exit(0)
