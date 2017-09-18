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


def changepassword(request):
	context = locals()
	signup = request.session.pop('signup', False)
	if (signup == False):
		return HttpResponseRedirect("/")
	else:
		request.session["signup"] = True
	if request.method == 'POST':
		print("ENTREEE222")
		formvar = request.POST
		if "exit" in formvar.keys(): 
			request.session["signup"] = False
			return HttpResponseRedirect("/")
		elif "back" in formvar.keys():
			request.session["signup"] = True
			return HttpResponseRedirect("/sambamanager/")
		elif "changeuser" in formvar.keys():
			context["USERCHANGE"] = str(formvar["changeuser"])
		elif "changeuserapplied" in formvar.keys():
			context["USERCHANGE"] = str(formvar["change_user"])
			if (str(formvar["change_repassword"]) == str(formvar["change_password"])):
				changeuser = str(formvar['change_user'])
				changepass= str(formvar["change_password"])
				changegroup = "NOWORK"
#				print(addgroup)
				headers = {'Content-type': 'application/json'}
				data = { 'username': changeuser, 'password': changepass, 'group': changegroup }
				context['MESSAGE'] = 'The user of ' + changeuser + ' was changed.'
				url = 'http://localhost:5000/samba/' + changeuser
				response = requests.put(url, data=json.dumps(data), headers=headers )
			else:
				context['MESSAGE'] = 'Different passwords' 
			
	return render(request, 'sambamanager/changepassword.html', context)

