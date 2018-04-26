from django.shortcuts import render_to_response
from django.http import HttpResponse

from .models import Bookshops,Books
# Create your views here.
def index(request):
	bookshop = Bookshops.objects.all()
	return render_to_response('cms/menu.html',locals())

