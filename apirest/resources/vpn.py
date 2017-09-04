import subprocess
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


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

