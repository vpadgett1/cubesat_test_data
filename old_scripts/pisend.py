import serial
import socket
import os
import time

ser = serial.Serial(port='/dev/ttyS3', baudrate=115200, timeout=.1)

hostname = socket.gethostname()  # IP address of host device
host = socket.gethostbyname(hostname)
port = 65432
HEADERSIZE = 10
WiFi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # attaching to IP and socket stream
WiFi.bind((host, port))  # bind to ip
print(f'socket bound to {host}:{port}')
WiFi.listen(5)


if os.path.exists('sampledata.csv'):
    print("path exists")
    with open('sampledata.csv', 'r') as f:
        lines = f.readlines()
        for line in lines:
            arr = bytes(line, 'utf-8')
            ser.write(arr)
            print("written")
            ser.flush()