import socket
import threading

device_chars = ["v", "g", "p"]  # Identifikátory zařízení, například 'v' pro volant

def handle_data(data):
    device = ""
    command = ""
    
    # Najde první znak odpovídající zařízení
    for char in data:
        if char in device_chars:
            device = char
            print(f"Identifikace zařízení: {device}")
        else:
            command += char
    print(f"Přijatý příkaz: {command}")

def handle_client(client_socket, addr):
    try:
        # Přijetí prvotní zprávy pro identifikaci zařízení
        data = client_socket.recv(1024).decode("utf-8")
        match data:
            case "volant":
                print(f"Připojení od {addr} je typu volant")
            case "pedaly":
                print(f"Připojení od {addr} je typu pedály")
            case "game":
                print(f"Připojení od {addr} je typu game")
            case _:
                print(f"Připojení od {addr} je typu neznámá")

        # Smyčka pro příjem a zpracování zpráv od klienta
        while True:
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                break

            # Ukončení spojení na základě příkazu "exit"
            if data.lower() == "exit":
                print(f"Klient {addr} ukončil spojení.")
                break

            # Zpracování přijatých dat
            handle_data(data)

            # Odpověď klientovi
            response = f"Potvrzeno: {data}"
            client_socket.send(response.encode("utf-8"))

    except ConnectionResetError:
        print(f"Spojení s klientem {addr} bylo přerušeno.")
    finally:
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 5656))
    server_socket.listen(5)
    print("Server běží na portu 5555...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Nové připojení od: {addr}")
        
        # Spuštění vlákna pro každého klienta
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()
