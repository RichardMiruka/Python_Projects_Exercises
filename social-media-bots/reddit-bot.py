import praw 

reddit = praw.Reddit(
    client_id="S48YmERmER0pz0oKgfzn3Q",
    client_secret="GqRKs-RccRn5ckPzsjthtKoi3--paw",
    user_agent="myBot/0.0.1",
)

reddit.user.me()

subreddit = reddit.subreddit("learnpython")
for submission in subreddit.hot(limit=5):
    print(submission.title)

# for submission in subreddit.stream.submissions():
   # print(submission.title)