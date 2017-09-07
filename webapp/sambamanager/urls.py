from django.conf.urls import url

#from . import views
from . import sambamenu

urlpatterns = [
#    url(r'^$', views.index, name='index'),
    url(r'^$', sambamenu.sambamenu, name='sambamenu'),
]
