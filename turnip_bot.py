#!/usr/bin/python
import praw
import time
import re

from selenium import webdriver

url = ''

browser = webdriver.Chrome()

reddit = praw.Reddit(client_id='mxKovfux0AzbgQ', client_secret='sksldmRIZaApy2vGr-kBn7H7MJo', user_agent='Turnip Queue Bot1.0')

subreddit = reddit.subreddit('acturnips')

print('Bot has started.')
while True:
    submission = list(subreddit.new(limit=1))[0]
    match = re.search('https://turnip.exchange/island/........', submission.selftext)
    if match:
        url = match.group(0)
        browser.get(url)
        break
    time.sleep(2)
