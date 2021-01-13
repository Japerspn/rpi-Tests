import time
import board
import busio
import adafruit_mpr121

import argparse
from pythonosc import udp_client

#set up argparser for OSC sending
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1")
  parser.add_argument("--port", type=int, default=5005)
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

#set up the capacitive touch board
i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)


while True:
    # Loop through all 12 inputs (0-11).
    for i in range(12):
        if mpr121[i].value:
            current_touched = i

            if current_touched != last_touched:
                print(f'{current_touched} touched!')

            last_touched = current_touched

    if not mpr121[current_touched].value and current_touched == last_touched:
        print(f'{current_touched} released!')

        current_touched = 100
        last_touched = 110

    time.sleep(0.1)
