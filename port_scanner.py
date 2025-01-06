import socket
from datetime import datetime

def port_scanner(target_ip):
    print(f"Starting scan on {target_ip}")
    common_ports = [22, 80, 443, 3389]  # Scan fewer common ports
    open_ports = []

    start_time = datetime.now()

    # Open a text file to save results
    with open("port_scan_results.txt", "w") as file:
        file.write(f"Port Scan Report for {target_ip}\n")
        file.write(f"Scan started at: {start_time}\n\n")

        for port in common_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)  # Shorter timeout
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
                print(f"[+] Port {port} is open")
                file.write(f"[+] Port {port} is open\n")
            sock.close()

        end_time = datetime.now()
        file.write(f"\nScan completed in: {end_time - start_time}\n")
        file.write(f"Open Ports: {open_ports}\n")

    print(f"\nScan results saved to port_scan_results.txt")

if __name__ == "__main__":
    target = input("Enter target IP address (e.g., 192.168.1.1): ")
    port_scanner(target)