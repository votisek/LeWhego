import socket
import time

info = {
    "pedaly": {"ip": ""},
    "volant": {"ip": ""},
    "game": {"ip": "46.135.68.171"},
    "host": {"hostip": "0.0.0.0", "rlip": "46.135.68.171"},
    "port": 65432
}

# Nastavení a připojení klienta k serveru
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((info["host"]["hostip"], info["port"]))
print("Připojeno k serveru.")

# Odesílání dat do serveru
data = "hello"
while True:
    client_socket.send(data.encode("utf-8"))
    server_response = client_socket.recv(1024).decode("utf-8")
    print(f"Odpověď serveru: {server_response}")
    time.sleep(1)  # Přestávka mezi odesíláním zpráv
