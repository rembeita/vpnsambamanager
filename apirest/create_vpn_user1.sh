#!/bin/bash
echo "Creating user $1"
cd /root/openvpn-ca
source vars
./build-key --batch $1

