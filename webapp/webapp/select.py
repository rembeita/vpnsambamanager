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
		context = locals()
		if "exit" in formvar.keys():
			return HttpResponseRedirect("/")
		signup = request.session.pop("signup", False)
		if (signup == True):
			if "samba_admin" in formvar.keys(): # (formvar.has_key('deleteuser')):
				request.session['signup'] = True
				return redirect("/sambamanager/")
			if "vpn_admin" in formvar.keys(): # (formvar.has_key('deleteuser')):
				request.session['signup'] = True
				return redirect("/vpnmanager/")
		else:
			uservalue = str(formvar['user_frm'])
			passvalue = str(formvar['password_frm'])
			print("entre")
			print(passvalue)
			userquery = authenticate(username=uservalue, password=passvalue)
			if userquery is None:
				message = "User or Password is incorrect."
				context['MENSAJE'] = message
				return render(request, 'general/invaliduserpass.html', context)
			else:
				request.session['signup'] = True
				return render(request, 'general/select.html', context)
	else:
		signup = request.session.pop("signup", False)
		if (signup == True):
			context = locals()
			request.session['signup'] = True

	return render(request, 'general/select.html', context)

