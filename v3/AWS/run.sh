#!/bin/bash

# start mosqitto service, remember to configure the mosqitto configuration file first
#
# When you run mosquitto, it will run with its default configuration. We need to change
# its configuration to allow for WebSocket connections (we want to visit the server from
# Javascript). To change the configuration of Mosquitto, we can modify the configuration
# file found at etc/mosquitto/mosquitto.conf. My configuration file
# contains these lines:
#
# listener 1883
# protocol mqtt
#
# listener 9002
# protocol websockets

sudo service mosquitto start
# run web server application
python app.py
