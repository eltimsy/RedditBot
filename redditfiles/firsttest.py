import praw
import pdb
import os
import re
import secrets
# from .secrets import (
#     CLIENTID,
#     CLIENTSECRET,
#     REDDITPASSWORD,
#     REDDITUSERNAME,
#     USERAGENT,
# )

reddit = praw.Reddit(client_id=secrets.CLIENTID,
                     client_secret=secrets.CLIENTSECRET,
                     password=secrets.REDDITPASSWORD,
                     username=secrets.REDDITUSERNAME,
                     user_agent=secrets.USERAGENT)

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit("pythonforengineers")

for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("I got all your money now!")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)
            with open("posts_replied_to.txt", "w") as f:
                for post_id in posts_replied_to:
                    f.write(post_id + "\n")
    # print("Title: ", submission.title)
    # print("Text: ", submission.selftext)
    # print("Score: ", submission.score)
    # print("---------------------------------\n")