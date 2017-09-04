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


def mainmenu(request):
	if request.method == 'POST':
		formvar = request.POST
		print(dir(formvar))
		uservalue = str(formvar['user_frm'])
		passvalue = str(formvar['password_frm'])
		context = locals()
		context['USER'] = uservalue
		context['PASS'] = passvalue
		userquery = authenticate(username=uservalue, password=passvalue)
		if userquery is None:
			message = "User or Password is incorrect."
			context['MENSAJE'] = message
			return render(request, 'sambamanager/invaliduserpass.html', context)

		print(formvar.keys())
		if "deleteuser" in formvar.keys(): # (formvar.has_key('deleteuser')):
			print("entre")
			deleteuser = str(formvar['deleteuser'])
			headers = {'Content-type': 'application/json'}
			url = 'http://localhost:5000/samba/' + deleteuser
			response = requests.delete(url, data=json.dumps(''), headers=headers )
			#users_list = getsambausers('http://localhost:5000/sambausers/')
			#context["users_list"] = users_list["users_list"]
			#return render(request, 'sambamanager/mainmenu.html', context)

	users_list = getsambausers('http://localhost:5000/sambausers/')
	context["users_list"] = users_list["users_list"]
	return render(request, 'sambamanager/mainmenu.html', context)

def getsambausers(url):
	response = requests.get(url)
	return response.json()
