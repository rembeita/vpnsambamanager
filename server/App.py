from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from Security import authenticate, identity
from Vault import *
import argparse
import subprocess
#####################
## Configuration
####################

token_lease_time = '5m'
token_num_uses = '5'
portsel = '80'
listeniface = '0.0.0.0'


#####################
app = Flask(__name__)
app.secret_key = "M3r1d14n"
api = Api(app)
jwt = JWT(app, authenticate, identity) # /auth

class SambaList(Resource):
#	@jwt_required()
	def get(self):
		output = subprocess.run("/usr/bin/pdbedit -L", shell=True, stdout=subprocess.PIPE, universal_newlines=True)
		result = self.parse_users(output.stdout)
		return {'users_list': result}, 200

	def parse_users(self, users_string):
		users_list = users_string.replace('\n', '').split(':')
		result_list = []
		result_dic = {}
		for i in range(len(users_list)):
			if ( i % 2 == 0):
				result_dic['username'] = users_list[i] 
			else:
				result_dic['id'] = users_list[i]
				result_list.append(result_dic)
				result_dic = {}	
		result_list
		return result_list


class Samba(Resource):
	#parser = reqparse.RequestParser()
	#parser.add_argument('username', type=str, required=True, help="This field cannot be blank.")
	#parser.add_argument('password', type=str, required=True, help="This field cannot be blank.")
	def post(self, name):
	#	data = Samba.parser.parse_args()
		output = subprocess.run("/usr/sbin/useradd " + name + " -g smbrestricted", shell=True, stdout=subprocess.PIPE, universal_newlines=True)
		print(output.stdout)
		cmd = subprocess.Popen('/usr/bin/smbpasswd -a ' + name , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True) 
		cmd.stdin.write(b'123\n')
		cmd.stdin.flush()
		print(cmd.stdout)
		cmd.stdin.write(b'123\n')
		cmd.stdin.flush()
		for line in cmd.stdout.readlines():
			print(line)
		return 200

	def delete(self, name):
		output = subprocess.run("/usr/bin/smbpasswd -x " + name , shell=True, stdout=subprocess.PIPE, universal_newlines=True)
		print(output.stdout)
		return 200		


class VPNList(Resource):
#	@jwt_required()
	def get(self):
		output = subprocess.run("/usr/bin/pdbedit -L", shell=True, stdout=subprocess.PIPE, universal_newlines=True)
		result = self.parse_users(output.stdout)
		return {'users_list': result}, 200


class VPN(Resource):
	#parser = reqparse.RequestParser()
	#parser.add_argument('username', type=str, required=True, help="This field cannot be blank.")
	#parser.add_argument('password', type=str, required=True, help="This field cannot be blank.")
	def post(self, name):
	#	data = Samba.parser.parse_args()
		output = subprocess.run("/home/rodrigo/vpnsambamanager/server/delete_vpn_user.sh " + name , shell=True, stdout=subprocess.PIPE, universal_newlines=True)
		print(output.stdout)
		return 200

	def delete(self, name):
	#	data = Samba.parser.parse_args()
		output = subprocess.run("/home/rodrigo/vpnsambamanager/server/delete_vpn_user.sh " + name , shell=True, stdout=subprocess.PIPE, universal_newlines=True)
		print(output.stdout)
		return 200

if __name__ == "__main__":
	api.add_resource(SambaList,'/sambausers/') 
	api.add_resource(Samba,'/samba/<string:name>') 
	api.add_resource(VPNList,'/vpnusers/') 
	api.add_resource(VPN,'/vpn/<string:name>') 
	app.run(host=listeniface,port=portsel)
