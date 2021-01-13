  GNU nano 3.2                                        oscTest.py

import argparse
import random
import time

from pythonosc import udp_client

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
