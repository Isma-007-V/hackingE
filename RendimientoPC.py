import time
import psutil

#cpu, memoria, disco 

def get_cpu_usage():
    return psutil.cpu_percent()

def get_memroy_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage('.').percent


def main():
    cpu_usage = 0
    memroy_usage = 0
    disk_usage = 0
#bucle para realizar lo que es iteracion
    while True:
        new_cpu_usage = get_cpu_usage()
        if new_cpu_usage > cpu_usage:
            print(f'CPU: {new_cpu_usage}')
        cpu_usage = new_cpu_usage

        new_memroy_usage = get_memroy_usage()
        if new_memroy_usage > memroy_usage:
            print(f'Memoria: {new_memroy_usage}')
            memroy_usage = new_memroy_usage


        new_disk_usage = get_disk_usage()
        if new_disk_usage > disk_usage:
            print(f'Disco: {new_disk_usage}')
            disk_usage = new_disk_usage

time.sleep(1)   

if __name__ == '__name__':
    main()
        