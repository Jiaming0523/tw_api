MINI PROJECT1 

1. Environment setup
tweepy           pip install tweepy
subprocess       pip install subprocess
ffmpeg           sudo apt-get update 
 
                 sudo apt-get install ffmpeg   
google_cloud_vision      pip install google-cloud-vision



2. Introduction
 Before running this program, you need to enter your twitter development keys and install google vision apis documents. Detailed procedures are as followed:
 pre claim the keys before in python program:
consumer_key = "your consumer key"
consumer_secret = "your soncumer secret key"
access_key = "your token access"
access_secret = "your token access secret"

 import google vision apis :
from google.cloud import vision
from google.cloud.vision import types


3. More sources
https://cloud.google.com/vision/docs/libraries
