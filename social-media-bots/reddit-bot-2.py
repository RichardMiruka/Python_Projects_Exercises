import praw 

reddit = praw.Reddit(
    client_id="S48YmERmER0pz0oKgfzn3Q",
    client_secret="GqRKs-RccRn5ckPzsjthtKoi3--paw",
    user_agent="myBot/0.0.1",
)

reddit.user.me()

reddit.subreddit("test").submit(
    title="My first reddit bot",
    selftext="Hello, I am a bot created by /u/RichardMiruka1234."
)
