import socket
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from sensor_data_pb2 import SensorData

INFLUXDB_URL = "http://localhost:8086"
INFLUXDB_TOKEN = "Kzplcruug9ZSiEaeQ9XInv5XAFTjxCXd34rvyv8s7uI61alK9HTAi8BiluCT5RjtWKTpFSS2d-kmBQvfsCHVZQ=="
INFLUXDB_ORG = "ss"
INFLUXDB_BUCKET = "sensor_data"
SERVER_ADDRESS = ('',50007)

def write_to_influxdb(sensor_data):
    with InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)
        point = Point("sensor_data") \
            .tag("device_id", sensor_data.device_id) \
            .field("event_id", sensor_data.event_id) \
            .field("humidity", sensor_data.humidity) \
            .field("temperature", sensor_data.temperature)
        write_api.write(bucket=INFLUXDB_BUCKET, record=point)
        print(f"Data written to InfluxDB: {sensor_data}")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(SERVER_ADDRESS)
        server_socket.listen()
        print("Server listening on", SERVER_ADDRESS)

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print("Connected by", addr)
                data = conn.recv(1024)
                if data:
                    sensor_data = SensorData()
                    sensor_data.ParseFromString(data)
                    print(f"Received data: {sensor_data}")
                    write_to_influxdb(sensor_data)

main()
