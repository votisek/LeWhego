import socket
import time
import 

device = "pedaly"

def get_data():


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("", 5656))

    try:
        # Odeslání identifikační zprávy na server
        client_socket.send(device.encode("utf-8"))

        while True:
            # Zadání zprávy od uživatele nebo automatické odeslání

            client_socket.send(get_data().encode("utf-8"))

            # Přijímání odpovědi od serveru
            response = client_socket.recv(1024).decode("utf-8")
            print(f"Server: {response}")

            # Pauza mezi zprávami (nastavitelná pro testování)
            time.sleep(1)

    except KeyboardInterrupt:
        print("Ukončuji spojení klávesou CTRL+C.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
