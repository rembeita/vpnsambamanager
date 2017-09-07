import subprocess
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class VPNList(Resource):
#	@jwt_required()
	def get(self):
		with open('/root/openvpn-ca/keys/index.txt') as f:
			read_data = f.read()
		f.closed
		result = self.parse_certs(read_data)
		print(result)
		return {'users_list': result}, 200

	def parse_certs(self, data):
		certs = data.split('\n')
		result = {}
		for i in certs:
			if ( i != ''):
				line = i.split('/')
				result[str(line[6]).replace("CN=","")] = line[0][0]
		#print(result)
		return result
		

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

