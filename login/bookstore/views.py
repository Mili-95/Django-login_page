from audioop import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import  messages
from .forms import Userform
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password



# Create your views here.
def login_form(request):
	return render(request, 'bookstore/login.html')


def logoutView(request):
	logout(request)
	return redirect('home')


def loginView(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request,f'welcome')
			return redirect(reverse('dashboard'))
		else:
			messages.info(request, "Invalid username")
			return redirect('home')		
        


def registerForm(request):
	return render(request, 'bookstore/register.html')


def registerView(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password = make_password(password)

		a = User.objects.create_user(username=username, email=email, password=password)
		a.save()
		messages.success(request, 'Account was creted sucessfully')
		return redirect('home')
	else:
		messages.error(request, ' Registration fail, try again')
		return redirect('regform')



def dashboardView(request):
    return render(request, 'dashboard/dashboard.html')    