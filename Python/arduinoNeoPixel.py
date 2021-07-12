import serial
from time import sleep

ard = serial.Serial(port='COM6', baudrate=115200, timeout=.1)



while True:
    [print(x) for x in ard.readlines()]
    y = input()
    ard.write(b"123")
    sleep(0.2)

x = "255,255,255:1,1,1,1,1,1,1"