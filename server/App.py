from flask import Flask
from flask_restful import Resource, Api
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

class Samba(Resource):
#	@jwt_required()
	def get(self):
		token = "rodrigo"
		#result = subprocess.call(['/usr/bin/pdbedit', '-L'], stdout=subprocess.PIPE)
		#print dir(result)
		#print result
		output = subprocess.run("/usr/bin/pdbedit -L", shell=True, stdout=subprocess.PIPE, universal_newlines=True)
		result = self.parse_users(output.stdout)
		return {'vault': result}

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


if __name__ == "__main__":
	api.add_resource(Samba,'/samba/') 
	app.run(host=listeniface,port=portsel)
