import praw
import time
from random import uniform

keywords = ['benghazi','hillary','obama','russia','maga','the wall', 'pie'] #keyword you want to match on		 
bot = praw.Reddit(user_agent='AutobotDetection', #same as username
				  client_id='SXgLBfwj0QSOEA', #comes from registration
				  client_secret='EFCmRkMofLwtsitefJvrks0-Sxs', #comes from registration
				  username='AutobotDetection', #username
				  password='4zjYtnH@M4SKhVfi') #password
subreddit= bot.subreddit('All') #decide which subs you want to scan for
comments = subreddit.stream.comments() 

for comment in comments:
	text = comment.body #text of the comment you matched on
	author = comment.author #comment author, good if you want to tag the other person
	

	if any(word in text.lower() for word in keywords) and author != 'AutobotDetection' and author != 'AutoModerator' and author != 'GoodBot_BadBot': #put username here so you dont match on yourself
		rand = uniform(10.0,97.0)
		message = ''.join(("Hello", " u/{0}".format(author),". Your comment history has prompted an inspection by Reddit's Admins.  \n",
					"Based on my deep machine learning, there is a ",repr(rand), " % chance that you are a bot.  \n",
					">If you feel this information is incorrect, please file a report to botdetection@reddit.com"  
		))
		try:
			comment.reply(message) #sends the message
		except praw.exceptions.APIException as e:
			if e.error_type == 'RATELIMIT':
				print("sleeping")
				time.sleep(60)
				print("leaving my sleep")
		except Exception as e:
			print(e)
		print(message) #prints to console for fun
		print("bot detected")
