#!/bin/bash
echo "Deleting user $1"
cd /root/openvpn-ca
source vars
./revoke-full $1
cp keys/crl.pem /etc/openvpn/
systemctl restart openvpn
