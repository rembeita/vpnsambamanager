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
import os
from django.views.static import serve
from django.utils.encoding import smart_str
from wsgiref.util import FileWrapper

def vpnmenu(request):
			
	signup = request.session.pop('signup', False)
	print(signup)
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
			url = 'http://localhost:5000/vpn/' + deleteuser
			context['MESSAGE'] = 'The user ' + deleteuser + ' was revoked.'
			response = requests.delete(url, data=json.dumps(''), headers=headers )
		if "adduser" in formvar.keys(): # (formvar.has_key('deleteuser')):
			adduser = str(formvar['username'])
			headers = {'Content-type': 'application/json'}
			url = 'http://localhost:5000/vpn/' + adduser
			context['MESSAGE'] = 'The user ' + adduser + ' was created.'
			response = requests.post(url, data=json.dumps(''), headers=headers )
		if "downloaduser" in formvar.keys(): # (formvar.has_key('deleteuser')):
			downloaduser = str(formvar['downloaduser'])
			filepath = '/root/client-configs/files/' 
			filenameovpn = downloaduser + '.ovpn'
			filename = filepath + filenameovpn
			wrapper = FileWrapper(open(filename))
			response = HttpResponse(wrapper, content_type='text/plain')
			response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(filename)
			response['Content-Length'] = os.path.getsize(filename)
			return response


	users_list = getvpnusers('http://localhost:5000/vpnusers/')
	context["users_list"] = users_list["users_list"]
	return render(request, 'vpnmanager/vpnmenu.html', context)

def getvpnusers(url):
	response = requests.get(url)
	return response.json()
