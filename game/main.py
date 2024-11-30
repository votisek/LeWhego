import socket
import threading
import vgamepad

gamepad = vgamepad.VX360Gamepad()

def handle_volant(data, minimal, maximal):
    if data == 0:
        gamepad.right_joystick_float(0, 0)
    elif data > 0:
        gamepad.right_joystick_float(data/maximal, 0)
    elif data < 0:
        gamepad.right_joystick_float(-1*(data/minimal), 0)
    


def handle_data(data, addr):
    if len(data) == 2: # Pedaly
        data_accelerator, data_brake = list(data)
        if data_accelerator is True:
            gamepad.right_trigger(255)
        elif data_accelerator is False:
            gamepad.right_trigger(0)
        if data_brake is True:
            gamepad.left_trigger(255)
        elif data_brake is False:
            gamepad.left_trigger(0)
    elif len(data) == 6: # Volant
        data_right_transmission, data_left_transmission, data_nitro, data_volant, min_volant, max_volant = list(data)
        if data_right_transmission is True:
            gamepad.press_button(button=vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        elif data_right_transmission is False:
            gamepad.release_button(button=vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        if data_left_transmission is True:
            gamepad.press_button(button=vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        elif data_left_transmission is False:
            gamepad.release_button(button=vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        if data_nitro is True:
            gamepad.press_button(button=vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_START)
        elif data_nitro is False:
            gamepad.release_button(button=vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_START)
        handle_volant(data=data_volant, minimal=min_volant, maximal=max_volant)
    else:
        print(f"Unknown data just came from {addr}")
    gamepad.update()

def handle_client(client_socket, addr):
    try:
        # Přijetí prvotní zprávy pro identifikaci zařízení
        data = client_socket.recv(1024).decode("utf-8")
        print(f"Připojení od {addr} s identifikací zařízení: {data}")
        
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
            handle_data(data, addr)


    except ConnectionResetError:
        print(f"Spojení s klientem {addr} bylo přerušeno.")
    finally:
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 5656))
    server_socket.listen(5)
    print("Server běží na portu 5656...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Nové připojení od: {addr}")
        
        # Spuštění vlákna pro každého klienta
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()
