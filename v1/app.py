#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
from flask import Flask


# GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

msg = "Null"


@app.route("/")  # at the end point /
def hello():  # call method hello
    return msg  # which returns "hello world"


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
    # set up GPIO
    GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
    GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

    # web setup
    app = Flask(__name__)  # create an app instance

    # infinite loop
    while True:
        time.sleep(1000)
        app.run(host='127.0.0.1', port=22)


if __name__ == "__main__":
    main()
