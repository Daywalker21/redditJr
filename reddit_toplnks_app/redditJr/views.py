from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from redditJr.models import User_data
import praw

# Create your views here.

client_id = "oFaFtViIHn-Oag"
client_secret = "5qI7bmlqOnPndkkQPw2TSjTmwCI"

@login_required
def home(request):
	if request.user.is_authenticated:

		r = praw.Reddit(client_id=client_id,
              	client_secret=client_secret,
              	redirect_uri = "http://127.0.0.1:8080" ,
              	user_agent="Using Django to find subreddit",
              	)


		print(request.user)

	return render(request,'html/index.html')
