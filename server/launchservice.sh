#!/bin/bash

cd /opt/server
#python3 App.py --port 6000 --vault-url http://192.168.0.117:8200 --access-token c31c22f8-e334-1a00-97b2-d2d2b15008a6 --listen 0.0.0.0

#python3 App.py --port 6000 --vault-url http://172.29.252.91:8200 --access-token 30b69947-5286-4f4e-a4bd-d5f2ac991796 --listen 0.0.0.0

python3 App.py --port $TRUSTED_SERVER_PORT --vault-url $TRUSTED_VAULT_URL --access-token $TRUSTED_VAULT_TOKEN --listen $TRUSTED_SERVER_IFACE
