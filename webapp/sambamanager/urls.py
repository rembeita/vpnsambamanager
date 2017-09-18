from django.conf.urls import url

#from . import views
from . import sambamenu
from . import changepassword

urlpatterns = [
#    url(r'^$', views.index, name='index'),
    url(r'^$', sambamenu.sambamenu, name='sambamenu'),
    url(r'changepassword/', changepassword.changepassword, name='changepassword'),
]
