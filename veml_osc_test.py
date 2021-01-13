import time
import board
import busio
import adafruit_veml7700
import argparse
import time
from pythonosc import udp_client

i2c = busio.I2C(board.SCL, board.SDA)
veml7700 = adafruit_veml7700.VEML7700(i2c)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default = "127.0.0.1",
        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=5005,
        help="The port the OSC server is listening on")
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)

    for x in range(10):
        client.send_message("/test", random.random())
        print("message sent")
        time.sleep(1)



while True:
    print("Ambient light:", veml7700.light)
    print("Lux:", veml7700.lux)
    client.send_message("/veml7700", [veml7700.light, veml7700.lux])

    time.sleep(0.1)
