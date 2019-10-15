#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import paho.mqtt.client as mqtt

HOST_IP = "192.287.39.934"

# GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

msg = "Null"


def callback(channel):
    if GPIO.input(channel):
        msg = "Water Detected! shutting down usb power"
        print(msg)
        os.system("sudo ~/uhubctl/uhubctl -p 2 -a 0")

    else:
        msg = "No Water! Opening usb power"
        print(msg)
        os.system("sudo ~/uhubctl/uhubctl -p 2 -a 0")


def main():
    # configure mqtt service
    client =mqtt.Client("RaspberryPi")
    client.connect(HOST_IP, port=9001, keepalive=60, bind_address="")

    # configure gpio
    GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
    GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

    # infinite loop
    while True:
        time.sleep(1000)
        client.publish("water",msg)


if __name__ == "__main__":
    main()
