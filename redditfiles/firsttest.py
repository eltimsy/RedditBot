import praw
from .secrets import (
    CLIENTID,
    CLIENTSECRET,
    REDDITPASSWORD,
    REDDITUSERNAME,
    USERAGENT,
)

reddit = praw.Reddit(client_id=CLIENTID,
                     client_secret=CLIENTSECRET,
                     password=REDDITPASSWORD,
                     username=REDDITUSERNAME,
                     user_agent=USERAGENT)

subreddit = reddit.subreddit("learnpython")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")