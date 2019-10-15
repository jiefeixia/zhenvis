#!/bin/bash

# Deply with this bash file before run the run.bash
sudo apt-get update

# install uhubctl to control usb port
sudo apt-get install libusb
git clone https://github.com/mvp/uhubctl
cd uhubctl
make

# install python GPIO control packageon
sudo apt-get install rpi.gpio

# install mqtt service
pip3 install paho-mqtt
