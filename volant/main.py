import socket
import time
import ev3dev2
import ev3dev2.sensor.lego as Sensor
import ev3dev2.sensor as SensorPort
import ev3dev2.motor as Motor
import time


left_transmission = Sensor.TouchSensor(SensorPort.INPUT_1)
right_transmission = Sensor.TouchSensor(SensorPort.INPUT_2)
volant = Sensor.GyroSensor(SensorPort.INPUT_3)
nitro = Sensor.TouchSensor(SensorPort.INPUT_4)
sound = ev3dev2.sound.Sound()


device = "volant"
valid_data = bool()
volant_data = [0, 0]
# volant_data in format: [max_left, max_right]


def get_volant_data():
    volant.calibrate()
    volant.reset()
    for i in range(2):
        while nitro.is_pressed is False:
            print("Waiting for button press")
        sound.play_tone(500, 100)
        for j in range(50):
            volant_data[i] += volant.angle
            time.sleep("0.05")
        volant_data[i] = volant_data / 50
        sound.play_tone(500, 100)

    

def get_volant():
    volant_angle = volant.angle
    if volant_angle > volant_data[1]:
        volant_angle = volant_data[1]
    elif volant_angle < volant_data[0]:
        volant_angle = volant_data[0]
    else:
        pass
    return volant_angle

    

def get_data():
    data_right_transmission = right_transmission.is_pressed
    data_left_transmission = left_transmission.is_pressed
    data_nitro = nitro.is_pressed
    data_volant = get_volant()
    min_volant, max_volant = volant_data
    return [data_right_transmission, data_left_transmission, data_nitro, data_volant, min_volant, max_volant]

def start_client():
    hub.speaker.beep(duration=100, frequency=500)
    get_volant_data()
    
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
