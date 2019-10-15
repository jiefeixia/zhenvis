#!/usr/bin/python
import paho.mqtt.client as mqtt
import time
import os
from flask import Flask

CLIENTID = "AWS"
msg = "Null"


@app.route("/")
def hello():  # call method hello
    global msg, CLIENTID
    return render_template('index.html', message=msg, client=CLIENTID)

def on_message(client, userdata, message):


def main():
    global CLIENTID
    # mqtt set up
    client = mqtt.Client(CLIENTID)  # create new instance
    # here we just connect AWS local host,
    # in the future we can deploy this client on other server to make more complacated function
    client.connect("127.0.0.1", port=9001, keepalive=60, bind_address="")
    client.subscribe("water")
    client.on_message = on_message
    client.loop_start()

    # web setup
    app = Flask(__name__)  # create an app instance

    app.run(host='127.0.0.1', port=22)


if __name__ == "__main__":
    main()
