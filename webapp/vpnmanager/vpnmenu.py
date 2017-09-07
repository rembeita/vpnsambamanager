from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
import requests
import json


def vpnmenu(request):
#	if request.method == 'POST':
#		formvar = request.POST
#		if "exit" in formvar.keys(): # (formvar.has_key('deleteuser')):
#			return HttpResponseRedirect("/sambamanager/")
#		print(dir(formvar))
#		uservalue = str(formvar['user_frm'])
#		passvalue = str(formvar['password_frm'])
#		context = locals()
#		context['USER'] = uservalue
#		context['PASS'] = passvalue
#		userquery = authenticate(username=uservalue, password=passvalue)
#		if userquery is None:
#			message = "User or Password is incorrect."
#			context['MENSAJE'] = message
#			return render(request, 'sambamanager/invaliduserpass.html', context)
#
#		print(formvar.keys())
#		elif "add_user" in formvar.keys(): # (formvar.has_key('deleteuser')):
#			if (str(formvar["add_repassword"]) == str(formvar["add_password"])):
#				adduser = str(formvar['add_user'])
#				headers = {'Content-type': 'application/json'}
#				data = { 'username': adduser, 'password': str(formvar["add_password"]) }
#				context['MESSAGE'] = 'The user ' + adduser + ' was created.'
#				url = 'http://localhost:5000/samba/' + adduser
#				response = requests.post(url, data=json.dumps(data), headers=headers )
#			else:
#				context['MESSAGE'] = 'Different passwords' 
			
	signup = request.session.pop('signup', False)
	if (signup == False):
		return HttpResponseRedirect("/")
	else:
		request.session["signup"] = True
	
	context = locals()
	if request.method == 'POST':
		formvar = request.POST
		if "deleteuser" in formvar.keys(): # (formvar.has_key('deleteuser')):
			deleteuser = str(formvar['deleteuser'])
			headers = {'Content-type': 'application/json'}
			url = 'http://localhost:5000/samba/' + deleteuser
			context['MESSAGE'] = 'The user ' + deleteuser + ' was eliminated.'
			response = requests.delete(url, data=json.dumps(''), headers=headers )

	users_list = getvpnusers('http://localhost:5000/vpnusers/')
	print(users_list)
	context["users_list"] = users_list["users_list"]
	return render(request, 'vpnmanager/vpnmenu.html', context)

def getvpnusers(url):
	response = requests.get(url)
	return response.json()
