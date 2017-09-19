#!/bin/bash
cd /home/rodrigo/vpnsambamanager
source bin/activate
cd apirest
python3 App.py > /tmp/rest.log 2>&1 &
cd ..
cd webapp
python3 manage.py runserver 0:80  > /tmp/django.log 2>&1 &

