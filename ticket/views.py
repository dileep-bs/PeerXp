# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect 
from django.contrib import messages 
from django.contrib.auth import authenticate 
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth.models import User
from django.contrib import auth
from .forms import TicketForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import AuthenticationForm 
from django.views.generic import ListView
from .models import Ticket
# Create your views here.



@csrf_exempt
def index(request):
	return render(request,'index.html')


class Alltickets(ListView):
	model = Ticket
	def get(self,request):
		alltickets = Ticket.objects.filter(username=request.user).all()
		return render(request,"viewtickets.html",{'alltickets':alltickets})
		
@csrf_exempt
def login(request):
	if request.method=='POST':
		# import pdb;pdb.set_trace()
		email=request.POST['email']
		password = request.POST['password']
		try:
			username= User.objects.get(email=email.lower()).username
			user=auth.authenticate(username=username,password=password)
		except User.DoesNotExist:
			return HttpResponse("please give valid email or password")
		if user is not None:
			form = auth_login(request,user)
			messages.success(request, 'wecome!!')
			return redirect('index')
		else:
			messages.info(request,'account done not exit plz sign in')
	form = AuthenticationForm() 
	return render(request, 'login.html', {'form':form, 'title':'log in'}) 


@csrf_exempt
def raise_ticket(request):
	print(request.POST)
	if request.method=='POST':
		# import pdb;pdb.set_trace()
		form=TicketForm(request.POST)
		username=(User.objects.get(id=request.POST['username']))
		if username==request.user:
			if form.is_valid():
				messages.success(request, 'successfully ticket rasied you!!')
				form.save()
				return redirect('index')
			else:
				form=TicketForm()
				return render(request,'raiseticket.html',{'form':form})
		else:
			return HttpResponse("Ticket Should be Raise by you only, please go back and check selected username")
	form=TicketForm()
	return render(request,'raiseticket.html',{'form':form})



def logout_request(request):
	auth_logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("index")
