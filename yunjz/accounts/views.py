from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login ad auth_login,logout as auth_logout

def index(request):
	username="supeihuang"
	return render(request,"accounts/index.html",{"username":username})
def register(request):
	if request.method=="POST":
		HttpResponseRedirect("accounts/index")
	return render(request,"accounts/register.html")

def login(request):
	template_var={}
	if request.method=='POST':
		username=request.POST.get("username")
		template_var={"error":"must first register","username":username}
	return render(request,"accounts/login.html",template_var,)
def logout(request):
	return render(request,"accounts/logout.html",)
# Create your views here.
