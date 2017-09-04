from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from Security import authenticate, identity
import argparse
from resources.samba import SambaList, Samba
from resources.vpn import VPNList, VPN


#####################
## Configuration
####################

portsel = '5000'
listeniface = '0.0.0.0'


#####################
app = Flask(__name__)
app.secret_key = "M3r1d14n"
api = Api(app)
jwt = JWT(app, authenticate, identity) # /auth

if __name__ == "__main__":
	api.add_resource(SambaList,'/sambausers/') 
	api.add_resource(Samba,'/samba/<string:name>') 
	api.add_resource(VPNList,'/vpnusers/') 
	api.add_resource(VPN,'/vpn/<string:name>') 
	app.run(host=listeniface,port=portsel)
