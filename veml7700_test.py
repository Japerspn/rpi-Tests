import time
import board
import busio
import adafruit_veml7700

i2c = busio.I2C(board.SCL, board.SDA)
veml7700 = adafruit_veml.VEML7700(i2c)

while True:
    print("Ambient light:", veml7700.light)
    print("Lux:", veml7700.lux)

    time.sleep(0.1)
