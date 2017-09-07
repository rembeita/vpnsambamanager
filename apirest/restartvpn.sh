#!/bin/bash
echo "Restarting VPN"
cp /root/openvpn-ca/keys/crl.pem /etc/openvpn/
systemctl restart openvpn
