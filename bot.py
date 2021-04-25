import praw

r = praw.Reddit("bot1")

subreddit = r.subreddit("cicada")
for sub in subreddit.hot(limit=10):
	print("-------------------------------------------")
	print(sub.title)
	
	for comment in sub.comments:
		if hasattr(comment, 'body'):
			comment_lower = comment.body.lower()
			if " sad " in comment_lower:
				print("*****")
				print(comment.body)