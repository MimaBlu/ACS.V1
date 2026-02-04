import socket

# Example firewall rule: block these IPs
blocked_ips = {
    "192.168.1.50",
    "10.0.0.99"
}

def start_firewall(port=8080):
    firewall_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    firewall_socket.bind(("0.0.0.0", port))
    firewall_socket.listen(5)

    print(f"[+] Firewall running on port {port}")

    while True:
        client_socket, client_addr = firewall_socket.accept()
        ip = client_addr[0]

        if ip in blocked_ips:
            print(f"[BLOCKED] Connection attempt from {ip}")
            client_socket.close()
            continue

        print(f"[ALLOWED] Connection from {ip}")
        client_socket.send(b"Connection allowed by simple firewall.\n")
        client_socket.close()

start_firewall()
