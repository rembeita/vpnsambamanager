import subprocess
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class SambaList(Resource):
#       @jwt_required()
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
	parser = reqparse.RequestParser()
	parser.add_argument('username', type=str, required=True, help="This field cannot be blank.")
	parser.add_argument('password', type=str, required=True, help="This field cannot be blank.")
	def post(self, name):
		data = Samba.parser.parse_args()
		output = subprocess.run("/usr/sbin/useradd " + data['username'] + " -g smbrestricted", shell=True, stdout=subprocess.PIPE, universal_newlines=True)
		print(data['username'])
		print(data['password'])
		print(output.stdout)
		cmd = subprocess.Popen('/usr/bin/smbpasswd -a ' + data['username'] , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True) 
		cmd.stdin.write(b''+ str(data['password']).encode('UTF-8') +b'\n')
		cmd.stdin.flush()
		print(cmd.stdout)
		cmd.stdin.write(b''+ str(data['password']).encode('UTF-8') +b'\n')
		cmd.stdin.flush()
		for line in cmd.stdout.readlines():
			print(line)
		return 200

	def delete(self, name):
		output = subprocess.run("/usr/bin/smbpasswd -x " + name , shell=True, stdout=subprocess.PIPE, universal_newlines=True)
		print(output.stdout)
		return 200		


