#!/usr/bin/python
import praw
import webbrowser
import time
import re

url = ''

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

reddit = praw.Reddit(client_id='mxKovfux0AzbgQ', client_secret='sksldmRIZaApy2vGr-kBn7H7MJo', user_agent='Turnip Queue Bot0.1')

subreddit = reddit.subreddit('acturnips')

print('Bot has started.')
while True:
    submission = list(subreddit.new(limit=1))[0]
    match = re.search('https://turnip.exchange/island/........', submission.selftext)
    if match:
        url = match.group(0)
        webbrowser.open_new(url)
        break
    time.sleep(2)
