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
		uservalue = str(formvar['user_frm'])
		passvalue = str(formvar['password_frm'])

	userquery = authenticate(username=uservalue, password=passvalue)

	context = locals()

	if userquery is None:
		message = "User or Password is incorrect."
		context['MENSAJE'] = message
		return render(request, 'sambamanager/invaliduserpass.html', context)

	users_list = getsambausers('http://localhost:5000/sambausers/')
	context['USER'] = uservalue
	context["users_list"] = users_list["users_list"]
	#print(user_list["users_list"])
	#user = data['user']
	for i in users_list["users_list"]:
		print(i)
	return render(request, 'sambamanager/mainmenu.html', context)

def getsambausers(url):
	response = requests.get(url)
	return response.json()
