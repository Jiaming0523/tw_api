# -*- coding: utf-8 -*-

#!/usr/bin/env python
# encoding: utf-8


import tweepy #https://github.com/tweepy/tweepy
import json
import sys
import wget
import urllib
import os
import io
import subprocess
from PIL import Image,ImageDraw,ImageFont

from google.cloud import vision
from google.cloud.vision import types
#Twitter API credentials


def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
          
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print ("...%s tweets downloaded so far" % (len(alltweets)))
    #get all urls from all tweets
    media_files = set()
    for status in alltweets:
        media = status.entities.get('media', [])
        if(len(media) > 0):
             media_files.add(media[0]['media_url'])
    num=1
 
    #download all urls and rename pictures with numbers
    i=0
    for url in media_files:
    	print(url)
    	urllib.request.urlretrieve(url,'/home/ece-student/picture/%d.jpg'%i)
    	i += 1


    #convert seriral pictures to vedio
def videooutput():
    os.system("ffmpeg -f image2 -r 0.2 -i /home/ece-student/picture/%01d.jpg  -vf 1350:-2 out.mp4")
 
   #attach labels to pictures using google apis
def label():
    #initialize google vision api
    client = vision.ImageAnnotatorClient()
    #get the number of pictures
    dir=path
    num=0
    for root,dirname,filenames in os.walk(dir):
        for filename in filenames:
            if os.path.splitext(filename)[1]=='.jpg':
                num = num +1

    #attach labels for every picture
    i=0
    while (i<num):
        file_name = os.path.join(os.path.dirname(__file__),path+'/'+str(i)+'.jpg')
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
        
if __name__ == '__main__':
    #pass in the username of the account you want to download
    screen_name=str(input("please input your screen name\n"))
    try:
        get_all_tweets(screen_name)
    except tweepy.error.TweepError as err:
        print("screen name dosn't exist")
    else
        path=os.getcwd()
        label()
        videooutput()
  
