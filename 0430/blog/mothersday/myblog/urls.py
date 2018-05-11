from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^delete$',views.delete, name='message_delete'),
	url(r'^create/$',views.save, name='message_create'),
	url(r'^update/$',views.update,name='message_update'),
	url(r'^',views.home, name='home'),
]