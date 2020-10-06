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
		# User_data.objects.create(user_name = request.user.username , subreddits = request.user.groups)
		# print(request.user._password)
		# reddit = praw.Reddit(client_id="nM4HdoqJHRz-Sg",
  #                    client_secret="xdI1iiBoMegWgs84M09R9SvRX8k",
  #                    password= request.user._password,
  #                    user_agent="testscript by u/fakebot3",
  #                    username=request.user.username)

		# subreddit = reddit.subreddit('python')

		# for s in subreddit.hot(limit = 5):
		# 	print(s.title)

		r = praw.Reddit(client_id=client_id,
              	client_secret=client_secret,
              	user_agent="Using Django to find subreddit"
              	)

		# r.set_oauth_app_info(
				
		# 	)

		subreddit = r.subreddit('python')
		
		for l in subreddit.hot(limit=5):
			print(l)

		# url = r.get_authorize_url('uniqueKey', 'identity', True)
		# access_information = r.get_access_information(request.user.password)
		
		# authenticated_user = r.get_me()
		# print(authenticated_user.name, authenticated_user.link_karma)

		print(request.user.get_username	)
	return render(request,'html/index.html')
