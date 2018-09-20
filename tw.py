# -*- coding: utf-8 -*-

#!/usr/bin/env python
# encoding: utf-8
#Author - Prateek Mehta


import tweepy #https://github.com/tweepy/tweepy
import json
import sys
import wget
import urllib
import os
import io
import subprocess

from google.cloud import vision
from google.cloud.vision import types
#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


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
       
    media_files = set()
    for status in alltweets:
        media = status.entities.get('media', [])
        if(len(media) > 0):
             media_files.add(media[0]['media_url'])
    num=1
 

    i=0
    for url in media_files:
    	print(url)
    	urllib.request.urlretrieve(url,'/home/ece-student/picture/%d.jpg'%i)
    	i += 1


    

    #write tweet objects to JSON
    #file = open('tweet.json', 'w') 
    #print ("Writing tweet objects to JSON please wait...")
    #for status in alltweets:
     #   json.dump(status._json,file,sort_keys = True,indent = 4)
#def videooutput():
 #   os.system("ffmpeg -f image2 -r 0.2 -i /home/ece-student/picture/%01d.jpg out.mp4")
    #close the file
    #print ("Done")
    #file.close()

def label():

    client = vision.ImageAnnotatorClient()
    dir=path
    num=0
    for root,dirname,filenames in os.walk(dir):
        for filename in filenames:
            if os.path.splitext(filename)[1]=='.jpg':
                num = num +1


    i=0
    while (i<num):
        file_name = os.path.join(os.path.dirname(__file__),path+'/'+str(i)+'.jpg')
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
        

        image = types.Image(content=content)
        response = client.label_detection(image=image)
        labels = response.label_annotations
        print('Labels:')
        for label in labels:
            print(label.description)
        i += 1
if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@Ladygaga")
    path=os.getcwd()
    label()
  
