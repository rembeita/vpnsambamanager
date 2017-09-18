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
		for i in range(len(users_list)-1):
			if ( i % 2 == 0):
				result_dic['username'] = users_list[i]
				result_dic['group'] = self.parse_groups(users_list[i])
			else:
				result_dic['id'] = users_list[i]
				result_list.append(result_dic)
				result_dic = {}
		result_list = sorted(result_list, key=lambda k: (k['group'], k['username'])) 
		return result_list

	def parse_groups(self, usergroup):
		getgroup = subprocess.run("/usr/bin/groups " + usergroup, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
		resp = str(getgroup.stdout).replace(' ','').replace('\n','').split(':')[1]
		return resp

class Samba(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('username', type=str, required=True, help="This field cannot be blank.")
	parser.add_argument('password', type=str, required=True, help="This field cannot be blank.")
	parser.add_argument('group', type=str, required=True, help="This field cannot be blank.")
	def post(self, name):
		data = Samba.parser.parse_args()
		if (data['group'] != "none"):
			output = subprocess.run("/usr/sbin/useradd " + data['username'] + " -g " + data["group"], shell=True, stdout=subprocess.PIPE, universal_newlines=True)
			print(data['username'])
			print(data['password'])
			print(data['group'])
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

	def put(self, name):
		data = Samba.parser.parse_args()
		print(data['username'])
		print(data['password'])
		cmd = subprocess.Popen('/usr/bin/smbpasswd -a ' + data['username'] , stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True) 
		cmd.stdin.write(b''+ str(data['password']).encode('UTF-8') +b'\n')
		cmd.stdin.flush()
		print(cmd.stdout)
		cmd.stdin.write(b''+ str(data['password']).encode('UTF-8') +b'\n')
		cmd.stdin.flush()
		for line in cmd.stdout.readlines():
			print(line)
		return 200
	
	def get(self, name):
		output = subprocess.run("/usr/bin/pdbedit -L " + name, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
		result = self.parse_users(output.stdout)
		return {'user': result}, 200
	
	def parse_users(self, users_string):
		users_list = users_string.replace('\n', '').split(':')
		result_list = []
		result_dic = {}
		for i in range(len(users_list)-1):
			if ( i % 2 == 0):
				result_dic['username'] = users_list[i]
				result_dic['group'] = self.parse_groups(users_list[i])
			else:
				result_dic['id'] = users_list[i]
				result_list.append(result_dic)
				result_dic = {}
		result_list = sorted(result_list, key=lambda k: k['username']) 
		return result_list

	def parse_groups(self, usergroup):
		getgroup = subprocess.run("/usr/bin/groups " + usergroup, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
		resp = str(getgroup.stdout).replace(' ','').replace('\n','').split(':')[1]
		return resp
