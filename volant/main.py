import socket
import time

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("94.241.92.90", 5656))

    try:
        client_socket.send("volant".encode("utf-8"))
        while True:
            # Zadání zprávy od uživatele
            message = input("Zadejte zprávu pro server: ")
            client_socket.send(message.encode("utf-8"))

            # Přijímání odpovědi od serveru
            response = client_socket.recv(1024).decode("utf-8")
            print(f"Server: {response}")

            # Pauza mezi zprávami (lze upravit nebo odstranit pro testování neustálé komunikace)
            time.sleep(1)

    except KeyboardInterrupt:
        print("Ukončuji spojení.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
