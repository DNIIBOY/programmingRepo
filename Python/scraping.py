import praw
import pandas as pd

reddit = praw.Reddit(client_id='WH5voxzOTogynw', client_secret='J5t4amNbKcabjjzGBYy0TrPWPKk', user_agent='Reddit Scraper')

posts = []
ml_subreddit = reddit.subreddit('All')
for post in ml_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
print(posts)

