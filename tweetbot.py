import tweepy
import time
import requests
from bs4 import BeautifulSoup
import lxml
import random



def scrape_some_data():
	r = requests.get('https://www.plot-generator.org.uk/story-ideas/').text
	soup=BeautifulSoup(r,'lxml')
	p = soup.find(class_='random_story').get_text()
	# deprecated code
	# rng = random.randrange(10,140)
	# op = p[:rng]
	# return op
	return p
	
CONSUMER_KEY = 'jIseBb65iypSqxyjD4Hsy8x8E'
CONSUMER_SECRET = 'VPp4wCLSfCJhOzNcmYT4XiS0DTiUmuCJ9ilK9taOoilxAr3JA4'
ACCESS_KEY = '857465526033031169-S5hLTgVmWyioAwzx6BWrUktOs14gC1w'
ACCESS_SECRET = 'ItCDglOvhhJcy27dYN82fQPOxTvqJ0f2xwvjoCdyC7rO5'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
	tweet = scrape_some_data()
	api.update_status(tweet)
	time.sleep(28800)





	