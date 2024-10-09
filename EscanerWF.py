from scapy.all import * 

def scan_network(ip_range):
    print(f"Escanenado Dispositivos en la rd {ip_range}")

    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_range), timeout=2, verbose=False)
    active_host = [res[1].psrc for res in ans]
    print("Dispositivos activos")
    for host in active_host:
        print(host)

if __name__ == "__main__":
    target_network = "192.168.1.0/24"
    scan_network(target_network)