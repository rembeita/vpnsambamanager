from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.shortcuts import redirect
import requests
import json


def select(request):
	if request.method == 'POST':
		formvar = request.POST
		print(formvar.keys())
		uservalue = str(formvar['user_frm'])
		passvalue = str(formvar['password_frm'])
		userquery = authenticate(username=uservalue, password=passvalue)
		context = locals()
		signup = request.session.pop("signup", False)
		if (signup == False):
			if userquery is None:
				print("entre2")
				message = "User or Password is incorrect."
				context['MENSAJE'] = message
				return render(request, 'general/invaliduserpass.html', context)
			else:
				print("entre1")
				request.session['signup'] = True
		else:
			request.session["signup"] = True
		#print(signup)
		#print(signup)
		if "samba_admin" in formvar.keys(): # (formvar.has_key('deleteuser')):
			request.session['signup'] = True
			print("Aca")
			return redirect("/sambamanager/")
		if "vpn_admin" in formvar.keys(): # (formvar.has_key('deleteuser')):
			request.session['signup'] = True
			print("Aca2")
			return redirect("/vpnmanager/")

	return render(request, 'general/select.html', context)

