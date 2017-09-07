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
		context = locals()
		context['USER'] = uservalue
		context['PASS'] = passvalue
		userquery = authenticate(username=uservalue, password=passvalue)
		if userquery is None:
			message = "User or Password is incorrect."
			context['MENSAJE'] = message
			return render(request, 'general/invaliduserpass.html', context)
		else:
			request.session['signup'] = True
		if "samba_admin" in formvar.keys(): # (formvar.has_key('deleteuser')):
			return HttpResponseRedirect("/sambamanager/")
		if "vpn_admin" in formvar.keys(): # (formvar.has_key('deleteuser')):
			return redirect("/vpnmanager/")

	return render(request, 'general/select.html', context)

