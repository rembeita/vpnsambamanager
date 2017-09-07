from django.conf.urls import url

from . import views
from . import vpnmenu

urlpatterns = [
#    url(r'^$', views.index, name='index'),
    url(r'^vpnmenu/$', vpnmenu.vpnmenu, name='vpnmenu'),
]
