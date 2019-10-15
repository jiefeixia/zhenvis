#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import paho.mqtt.client as mqtt


HOST_IP = "192.287.39.934"

# GPIO SETUP
SENSOR_GPIO = 21
RELAY_GPIO = 17
water = False

def callback(channel):
    if GPIO.input(channel):
        print("Water Detected!")
        water = True
        os.system("sudo ~/uhubctl/uhubctl -p 2 -a 0")

    else:
        print("No Water")
        water = False
        os.system("sudo ~/uhubctl/uhubctl -p 2 -a 0")


def main():
    # configure mqtt service
    client =mqtt.Client("RaspberryPi")
    client.connect(HOST_IP, port=9001, keepalive=60, bind_address="")

    # configure gpio
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_GPIO, GPIO.IN)
    GPIO.setup(RELAY_GPIO, GPIO.OUT) # GPIO Assign mode

    GPIO.add_event_detect(SENSOR_GPIO, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
    GPIO.add_event_callback(SENSOR_GPIO, callback)  # assign function to GPIO PIN, Run function on change


    # infinite loop
    while True:
        time.sleep(1000)
        if !water:
            GPIO.output(RELAY_GPIO, GPIO.HIGH) # on
            msg = "less water, watering"
        else:
            GPIO.output(RELAY_GPIO, GPIO.LOW) # on
            msg = "enough water, stop watering"

        # send message
        client.publish("water", msg)


if __name__ == "__main__":
    main()
