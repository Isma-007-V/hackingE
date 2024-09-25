from googlesearch import search

b = input("QUE DESEAS BUSCAR ?: ")

for bus in search(b, sleep_interval=5, num_results=10):
    print(bus)

