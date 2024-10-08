import nmap

scanner = nmap.PortScanner()

scanner.scan('172.67.73.188','1-1024','-v -sS -sV -sC -A -O')

for host in scanner.all_hosts():
    print("Host: ", host)
    for proto in scanner[host].all_protocols():
        lport = scanner[host][proto].keys()
        for port in lport:
            print("Port:", port)
            print("Name:", scanner[host][proto][port]['name'])
            print("State:", scanner[host][proto][port]['state'])
            print("Service:", scanner[host][proto][port]['name'])
            print("Version:", scanner[host][proto][port]['version'])
            
            if 'product' in scanner[host][proto][port]:
                print("Product:", scanner[host][proto][port]['product'])
            if 'extrainfo' in scanner[host][proto][port]:
                print("Extra Info:", scanner[host][proto][port]['extrainfo'])
                print("---------------------------------------------------")