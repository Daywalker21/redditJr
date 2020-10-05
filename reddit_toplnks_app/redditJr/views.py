from django.shortcuts import render
from django.http import HttpResponse
# from redditJr.models import user_data

# Create your views here.

client_id = "oFaFtViIHn-Oag"
client_secret = "5qI7bmlqOnPndkkQPw2TSjTmwCI"

def home(request):
	return render(request,'html/index.html')


def login_page(request):
	return render(request,'accounts/login')