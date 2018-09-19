# tw_api
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# encoding: utf-8
#Author - Prateek Mehta


import tweepy #https://github.com/tweepy/tweepy
import json
import sys
import wget

#Twitter API credentials
consumer_key = "jfW2IxwXDeLZ0o4cna16rITPy"
consumer_secret = "FpuJHKCixotvKtKZNzwMNNIBDBxoCKz0fRA3q1zzzHGrzOwSF9"
access_key = "1041024802125963264-lVPXOYNwBss9X3jHI76Jymuis9449U"
access_secret = "v0AMgvUb092S4to6zNws8P329DoSGXiPOgyU4X2kNXo0e"


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
 
    for url in media_files:
    	print(url)
    	urllib.request.urlretrieve(url,'/home/ece-student/picture/%d.jpg'%i)
    	i += 1
def videooutput():
    os.system("ffmpeg -i /home/ece-student/picture/%d.jpg -y test.mp4")
    #close the file
    #print ("Done")
    #file.close()
        
        #write tweet objects to JSON
    #file = open('tweet.json', 'w') 
    #print ("Writing tweet objects to JSON please wait...")
    #for status in alltweets:
     #   json.dump(status._json,file,sort_keys = True,indent = 4)
    
    #close the file
    #print ("Done")
    #file.close()

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@real")
    videooutput()
