from keys import C,b,AccessToken,AccessTokenSecret
import tweepy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import tkinter
import json
import collections
import flag
nltk.download('stopwords')
from paralleldots import set_api_key , get_api_key


import paralleldots

oauth = tweepy.OAuthHandler(C,b)
oauth.set_access_token(AccessToken,AccessTokenSecret)
api = tweepy.API(oauth)

user=api.me()
print(user.name)
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print("followed everyone that is following:"+ user.name)

a=[]
example='Hi my name is Shivangi Chauhan'
stop_words=stopwords.words('english')
list1=example.split()
for word in list1:
    if word not in stop_words:
        a.append(word)
        print(list1)
        print(a)

#update
def update_status():
    update_status=api.update_status(status="what's going on!")
    print(update_status)


def tweet_location():
    tweets=input("enter hashtags to search")
    tweet1=api.search(tweets)
    for search_result in tweet1:
        print('location',search_result.user.location)
        print('time_zone',search_result.user.time_zone)
        print('language',search_result.user.lang)

def sentiments():
    print("\nSentiments")
    print(paralleldots.sentiment("you are wrong")["sentiment"])

#def display_menu():
 #   global flag
  #  message = str
   # while flag == True:
    #    print("MENU")
     #   print("1.Retrieve Tweets")
      #  print("2.Count the followers")
       # print("3.Determine the sentiments")
        #print("4.Location, Language ,Time Zone")
        #print("5.Compare Tweets")
        #print("6.Analyze The Top usage")
        #print("7.Tweet a message")
        #print("8.Exit")
        #option=int(input("what do you want:?"))
        #if option==1:
        #    Get_Search()
         #   display_menu()
        #elif option==2:
         #   fcount()
          #  display_menu()
        #elif option==3:
         #   sentiment_analysis()
         #   display_menu()
        #elif option==4:
         #   location()
          #  display_menu()
        #elif option==5:
         #   compare()
          #  display_menu()
        #elif option==6:
         #   top_usage()
         #   display_menu()


user_tweets = api.user_timeline('shivangi chauhann')
for tweet in user_tweets:
    print(tweet.text)
    print (user.followers_count)

user1 = api.get_user('realDonaldTrump')
print("Name:",user1.name)
print("Location:",user1.location)
print("Following:",user1.friends_count)
print("Followers:",user1.followers_count)


