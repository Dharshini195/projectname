from django.shortcuts import render, redirect
from appname.forms import CreateUserForm 

from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required 
 

def register(request):	
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Your Account has been created for '+ user)
			return redirect('appname:login_reg')


	context = { 'form': form }
	return render (request, 'signin/register.html', context)


def login_reg(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('appname:index.html')
		else:
			messages.info(request, "Username Or password is incorrect.")


	context = {}
	return render (request, 'signin/login.html', context)

def logoutuser(request):
	logout(request)
	# return redirect('appname:login_reg')
	return redirect('appname:home')


@login_required(login_url = 'appname:login_reg')
def base(request):
	return render (request,"signin/base.html", context = {})


from django.shortcuts import render

# Create your views here.
def about(request):
    return render (request, 'about.html')

def contact(request):
    return render (request, 'contact.html')

def index(request):
    return render (request, 'index.html')

def portfoliodetails(request):
    return render (request, 'portfolio-details.html')

def portfolio(request):
    return render (request, 'portfolio.html')

def resume(request):
    return render (request, 'resume.html')

def services(request):
    return render (request, 'services.html')

