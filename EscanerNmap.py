import nmap 

scanner = nmap.PortScanner()
scanner.scan('172.67.73.188', '1,1024')
print(scanner['172.67.73.188'].all_protocols())
print(scanner['172.67.73.188'].state())
print(scanner['172.67.73.188']['tcp'].keys())