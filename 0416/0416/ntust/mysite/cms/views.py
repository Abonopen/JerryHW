from django.shortcuts import render_to_response
from django.http import HttpResponse

from .models import Myself,member
# Create your views here.
def index(request):
	myself = Myself.objects.all()
	return render_to_response('cms/menu.html',locals())

