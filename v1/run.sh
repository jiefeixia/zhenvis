#!/bin/bash

# read socketxp service
# socketxp will connect localhost with remote server
# expected output should be like "Tunnel Access -> tunnel.socketxp.com:35277"
echo -e "you can visit the website from:"
website = < <(socketxp -connect tcp://localhost:22)
echo website


# run web server application
python app.py
