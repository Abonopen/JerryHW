from django.shortcuts import render,redirect
from .models import Message
import datetime
from django.http import  HttpResponseRedirect
# Create your views here.
def home(request):
	message=Message.objects.all()
	return render(request,'myblog/home.html',locals())

def save(request):
	message=Message.objects.all()
	if request.method == "POST":
		auther = request.POST.get("auther","Guest")
		title = request.POST.get("title","None")
		content = request.POST.get("message","none")
		date= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
		m=Message.objects.create(auther=auther,title=title,content=content,date=date)
		m.save()
		return redirect('/home')
	else:
		return render(request,'myblog/create.html',locals())
	
def update(request):
	message = Message.objects.all()
	message_id = request.GET.get("m_id","")
	if request.method == 'GET':
		o = Message.objects.get(pk=message_id)
		return render(request,'myblog/update.html',locals())


	elif request.method == "POST":
		auther = request.POST["auther"]
		title = request.POST["title"]
		content = request.POST["message"]
		date= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		Message.objects.filter(pk=message_id).update(auther=auther,title=title,content=content,date=date) 
		return redirect('/home')

	else:
		return render(request, "myblog/home.html", locals())

def delete(request):
	post = Message.objects.get(pk=request.GET["d_id"])
	post.delete()
	return redirect('/home')

