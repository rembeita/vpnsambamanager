#!/bin/bash
#1- Connect as root doing sudo su and put the password if needed
sudo su
#2- Go to the root directory
cd /root
#3- Go to the openvpn-ca directory
cd /root/openvpn-ca
#4- Read variables
source vars
#5- Create SSL key for the client (USER CAN BE Any name)
# ./build-key USER
#6 - Go to the client-configs directory
# cd /root/client-configs
#7- Build Openvpn Configuration file (Remember to put the same name as the STEP 5)
# ./make_config.sh USER
#8- Copy the configuration file to some place and grab it with WINSCP for example
# cp files/USER.ovpn /tmp

