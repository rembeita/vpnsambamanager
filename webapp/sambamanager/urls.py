from django.conf.urls import url

from . import views
from . import mainmenu

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mainmenu$', mainmenu.mainmenu, name='mainmenu'),
]
