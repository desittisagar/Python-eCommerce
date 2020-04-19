from django.contrib.auth import authenticate, login, get_user_model

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ContactForm, Loginform, Registerform

def homepage(request):
	context = {
	"title":"This is home page",
	"premium":"Yeaahhh",
	}

	return render(request, "home_page.html", context)

def aboutpage(request):
	context = {
	"title":"This is about page"
	}
	return render(request, "home_page.html", context)

def contactpage(request):
	form_content = ContactForm(request.POST or None)
	context = {
	"title":"This is contact page",
	"form" : form_content
	}
	if form_content.is_valid():
		print(form_content.cleaned_data)
	# if request.method == 'POST':
	# 	print(request.POST)
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email'))
		#print(request.POST.get['fullname'])
	return render(request, "contact/view.html", context)	

def loginpage(request):
	form_login = Loginform(request.POST or None)
	context = {
	"form":form_login,
	}
	print(request.user.is_authenticated())
	if form_login.is_valid():
		username = form_login.cleaned_data.get("username")
		password = form_login.cleaned_data.get("password")
		user = authenticate(request, username = username, password = password)
		print(user)
		print(request.user.is_authenticated())
		if user is not None:
			login(request,user)
			return redirect("/")
		else:
			print("error")	
	
	return render(request, "auth/login.html",context)

User = get_user_model()

def registerpage(request):
	form_register = Registerform(request.POST or None)
	context = {
	"form":form_register,
	}
	if form_register.is_valid():
		print(request.POST['username'])
		print(form_register.cleaned_data)
		username = request.POST['username']#form_register.cleaned_data.get("username")
		#print(username)
		email = form_register.cleaned_data.get("email")
		password = form_register.cleaned_data.get("password")
		new_user = User.objects.create_user(username, email, password)
		print(email)
		#new_user.save()
		#print(new_user)

	return render(request, "auth/register.html",context)	


def homepage_old(request):
	html_ = """<!doctype html>
	<html lang="en">
	  <head>
	    <!-- Required meta tags -->
	    <meta charset="utf-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	    <!-- Bootstrap CSS -->
	    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

	    <title>Hello, world!</title>
	  </head>
	  <body>
		<div class = "text-center">
	    <h1>Hello, world!</h1>
	    </div>
	    <!-- Optional JavaScript -->
	    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
	    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
	    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
	    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
	  </body>
	</html>

	"""
	return HttpResponse(html_)