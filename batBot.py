import praw
import configparser
import re
config = configparser.ConfigParser()
config._interpolation = configparser.ExtendedInterpolation()
config.read('config.ini')


keyword = 'bat' #keyword you want to match on
symbolTop = """
              _,     _   _    ,_              
           o888P     Y8o8Y     Y888o.           
         d88888      88888      88888b         
       ,8888888b_  _d88888b_  _d8888888,       
       888888888888888888888888888888888       
"""
symbolBottom = """
       888888888888888888888888888888888
        Y8888P"Y888P"Y888P-Y888P"Y88888'
         Y888   '8'   Y8P   '8'   888Y
          '8o          V          o8'
"""

testMessage = "Did you summon me u/{0} ?"

# def calcCenter(word):



bot = praw.Reddit(user_agent=config.get('bat', 'user_agent'),
	client_id=config.get('bat', 'client_id'),
	client_secret=config.get('bat', 'client_secret'),
	username=config.get('bat', 'username'),
	password=config.get('bat', 'password'))
subreddit= bot.subreddit('All') #decide which subs you want to scan for
comments = subreddit.stream.comments() 

for comment in comments:
	text = comment.body #text of the comment you matched on
	author = comment.author #comment author, good if you want to tag the other person

	if keyword in text.lower() and author != 'batb0t' and author != 'AutoModerator' and comment.subreddit.banned != 'true': #put username here so you dont match on yourself
		#pattern = re.compile('[bat]^\s+')
		#match = pattern.match(text)
		#specialWord = match.group()
		#re.search('\bBat \b')
		message = ' '.join(("    ",
					symbolTop,
					testMessage.center(40," ").format(author),
				   symbolBottom,
				   "" #tags the author in the post for more fun
		))
		try:
			comment.reply(message) #sends the message
			print(message)
		except Exception as e:
			print(e) #print the message to the console so you an see it too

for comment in bot.inbox.unread():
	text = comment.body #text of the comment you matched on
	author = comment.author
	if 'yes' in text.lower() and author != 'batb0t' and author != 'AutoModerator' and comment.subreddit.banned != 'true':
		message = ' '.join(('I am here for you u/{0}'.format(author)))

	if 'no' in text.lower() and author != 'batb0t' and author != 'AutoModerator' and comment.subreddit.banned != 'true':
		message = ' '.join(('I am not here for you u/{0}'.format(author)))
	
	else:
		message = ' '.join(('I don\'t understand  you u/{0} !!!!'.format(author))) 	

	try:
			#comment.reply(message) #sends the message
			print(message)
	except Exception as e:
			print(e) #print the message to the console so you an see it too