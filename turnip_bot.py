#!/usr/bin/python
import praw
import time
import re

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(3)

name = 'Andrew'

reddit = praw.Reddit(client_id='mxKovfux0AzbgQ', client_secret='sksldmRIZaApy2vGr-kBn7H7MJo',
                     user_agent='Turnip Queue Bot1.0')

subreddit = reddit.subreddit('acturnips')

url = ''

print('Bot has started.')
while True:
    submission = list(subreddit.new(limit=1))[0]
    match = re.search('https://turnip.exchange/island/........', submission.selftext)
    if match:
        try:
            if url != match.group(0):
                url = match.group(0)
                driver.execute_script("window.open('{}');".format(url))
                driver.find_element_by_xpath("//button[contains(text(),'Join this queue')]").click()
                time.sleep(.5)
                driver.find_element_by_xpath('//input').send_keys(name)
                time.sleep(.5)
                driver.find_element_by_xpath("//button[contains(text(),'Join')]").click()
                time.sleep(.5)
        except:
            print('Damn... queue is full or post was bot resistant....')
    time.sleep(2)
