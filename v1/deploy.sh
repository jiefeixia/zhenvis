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

# install socketxp to break throgh the enterprise wifi if you don't have a static IP address
curl -O https://portal.socketxp.com/download/linux/socketxp && chmod +wx socketxp && sudo mv socketxp /usr/local/bin
# configure socketxp
# replace it with your own token here, to get a token, register your account at https://portal.socketxp.com
$ socketxp -register "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NDk1MTg0MDAsImlkIjoiZ2FuZXNodmVscmFqYW5AZ21ha6K208n0.cB2uYevpH4lWIQGQUJdQ0eiEDqS8OiP_YOiqernnui3rjjadfadsfsfas34"
if [ -z "$token" ]; then
    echo -e "please fill in your own token in the bash file"
    exit 1
fi
# install flask as web server packageon python
conda install flask
