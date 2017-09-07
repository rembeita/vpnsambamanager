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
	context = locals()
	signup = request.session.pop('signup', False)
	if (signup == False):
		return HttpResponseRedirect("/")
	else:
		request.session["signup"] = True
	if request.method == 'POST':
		formvar = request.POST
		if "exit" in formvar.keys(): # (formvar.has_key('deleteuser')):
			return HttpResponseRedirect("/")
		elif "deleteuser" in formvar.keys(): # (formvar.has_key('deleteuser')):
			deleteuser = str(formvar['deleteuser'])
			headers = {'Content-type': 'application/json'}
			url = 'http://localhost:5000/samba/' + deleteuser
			context['MESSAGE'] = 'The user ' + deleteuser + ' was eliminated.'
			response = requests.delete(url, data=json.dumps(''), headers=headers )
		elif "add_user" in formvar.keys(): # (formvar.has_key('deleteuser')):
			if (str(formvar["add_repassword"]) == str(formvar["add_password"])):
				adduser = str(formvar['add_user'])
				headers = {'Content-type': 'application/json'}
				data = { 'username': adduser, 'password': str(formvar["add_password"]) }
				context['MESSAGE'] = 'The user ' + adduser + ' was created.'
				url = 'http://localhost:5000/samba/' + adduser
				response = requests.post(url, data=json.dumps(data), headers=headers )
			else:
				context['MESSAGE'] = 'Different passwords' 
			
			

	users_list = getsambausers('http://localhost:5000/sambausers/')
	context["users_list"] = users_list["users_list"]
	return render(request, 'sambamanager/mainmenu.html', context)

def getsambausers(url):
	response = requests.get(url)
	return response.json()
