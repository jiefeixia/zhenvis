#!/bin/bash

# Deply with this bash file before run the run.bash
sudo apt-get update

# install mosqitto
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
sudo apt-get update
sudo apt-get install mosquitto
sudo apt-get install mosquitto-clients

# install mqtt service
pip3 install paho-mqtt flask
