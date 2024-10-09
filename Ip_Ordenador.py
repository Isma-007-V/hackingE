import socket

hostname = socket.gethostname()

ip = socket.gethostbyname(hostname)

print("El sonmbre de mi ordenador es: " +hostname)
print("la direccion IP es: " +ip )