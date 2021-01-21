import praw
import csv

reddit = praw.Reddit(client_id='', client_secret='', user_agent='my_user_agent')

# get 10 hot posts from the MachineLearning subreddit
posts = reddit.subreddit('Azure').new(limit=10000)

with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ['title','selftext','flair','url']
    csvfile.seek(0)
    csvfile.truncate()
    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for post in posts:
        title = post.title.encode('utf-8')
        selftext = post.selftext.encode('utf-8')
        link_flair_text = post.link_flair_text
        url = post.url.encode('utf-8')
        writer.writerow({'title':title,'selftext':selftext,'flair':link_flair_text,'url':url})