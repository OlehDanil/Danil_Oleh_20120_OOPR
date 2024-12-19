import socket
import time
import random
from sensor_data_pb2 import SensorData

SERVER_ADDRESS = ('localhost', 50007)
DEVICE_ID = "sensor_001"

def main():
    event_id = 0
    while True:
        try:
            # Генерация случайных данных
            humidity = random.uniform(30.0, 50.0)
            temperature = random.uniform(20.0, 40.0)
            event_id += 1

            # Формирование сообщения
            sensor_data = SensorData(
                device_id=DEVICE_ID,
                event_id=event_id,
                humidity=humidity,
                temperature=temperature
            )
            serialized_data = sensor_data.SerializeToString()

            # Отправка данных на сервер
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect(SERVER_ADDRESS)
                client_socket.sendall(serialized_data)
                print(f"Sent data: {sensor_data}")

        except (ConnectionRefusedError, socket.error) as e:
            print(f"Connection failed: {e}. Retrying in 1 second.")
        
        time.sleep(1)

main()
