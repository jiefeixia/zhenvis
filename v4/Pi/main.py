#!/usr/bin/python
import os
import time

import RPi.GPIO as GPIO
import json
import paho.mqtt.client as mqtt
import requests

HOST_IP = "192.287.39.934"

# GPIO SETUP
SENSOR_GPIO = 21
RELAY_GPIO = 17


def callback(channel):
    global water
    if GPIO.input(channel):
        print("Water Detected!")
        water = True
        os.system("sudo ~/uhubctl/uhubctl -p 2 -a 0")

    else:
        print("No Water")
        water = False
        os.system("sudo ~/uhubctl/uhubctl -p 2 -a 0")


def main():
    # Configure URL
    api_key = "Your_API_Key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Pittsburgh"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # configure mqtt service
    client = mqtt.Client("RaspberryPi")
    client.connect(HOST_IP, port=9001, keepalive=60, bind_address="")

    # configure gpio
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_GPIO, GPIO.IN)
    GPIO.setup(RELAY_GPIO, GPIO.OUT)  # GPIO Assign mode

    GPIO.add_event_detect(SENSOR_GPIO, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
    GPIO.add_event_callback(SENSOR_GPIO, callback)  # assign function to GPIO PIN, Run function on change

    # infinite loop
    while True:
        time.sleep(1000)

        # get weather json response
        response = requests.get(complete_url)
        x = response.json()

        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]

        msg = "Enough water" if water else "less water"
        low_humidity = True if (current_humidiy < 90) else False

        global water

        if (not water) and low_humidity:
            GPIO.output(RELAY_GPIO, GPIO.HIGH)  # on
            msg += "\nlow humanity, watering"
            watering = True
        else:
            GPIO.output(RELAY_GPIO, GPIO.LOW)  # on
            watering = False

        msg = {
            "time": datatime.now(),
            "temp": current_temperature,
            "pressure": current_pressure,
            "humidity": current_humidiy,
            "enoughWater": water,
            "watering": watering
        }

        # save log file
        if not os.path.isfile("log.csv"):
            with open('log.csv', 'a') as fd:
                fd.write("time,temp,pressure,humidity,enoughWater,watering\n")
                fd.write(f'{msg["time"]}, {msg["temp"]},{msg["pressure"]},{msg["humidity"]},{msg["enoughWater"]},'
                         f'{msg["watering"]}\n')
        else:
            with open('log.csv', 'a') as fd:
                fd.write(f'{msg["time"]}, {msg["temp"]},{msg["pressure"]},{msg["humidity"]},{msg["enoughWater"]},'
                         f'{msg["watering"]}\n')

        # send message
        client.publish("water", json.dumps(msg))


if __name__ == "__main__":
    main()
