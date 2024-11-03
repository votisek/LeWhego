import socket
import time

# Konfigurace
info = {
    "pedaly": {"ip": ""},
    "volant": {"ip": ""},
    "game": {"ip": "46.135.68.171"},
    "host": {"hostip": "0.0.0.0", "rlip": "46.135.68.171"},
    "port": 65432
}

# Vytvoření socketu klienta
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Připojení klienta k serveru
    client_socket.connect((info["host"]["rlip"], info["port"]))
    print("Připojeno k serveru.")

    # Odesílání dat do serveru
    while True:
        data = "hello"  # Zde můžete změnit zprávu, kterou chcete poslat
        client_socket.send(data.encode("utf-8"))  # Odeslání dat na server
        
        # Čekání na odpověď od serveru
        server_response = client_socket.recv(1024).decode("utf-8")
        print(f"Odpověď serveru: {server_response}")
        
        time.sleep(1)  # Přestávka mezi odesíláním zpráv

except ConnectionRefusedError:
    print("Nelze se připojit k serveru - spojení odmítnuto.")
except Exception as e:
    print(f"Chyba klienta: {e}")
finally:
    # Uzavření socketu
    client_socket.close()
    print("Klient byl ukončen.")
