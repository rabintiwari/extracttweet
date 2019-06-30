import tweepy
from textblob import TextBlob
import re

consumer_key = 'H19KtK5P7cMSqJXc1bsR4N8H8'
consumer_secret = 'BNIRME2GK6KDVnTQ7H1HBRO7QdU6mUSOnevKRwvu4aX17m0OrR'

access_token = '1104423154691256320-fSRp8U1VcZAW83UknLRw1aQGqzvScT'
access_token_secret = 'fW4ISP2TPGXe964sfi18joL2UfVtjRZwcIS2OYig3osw0'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

def clean_tweet(self, tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t\n\])|(\w+:\/\/\S+)", " ", tweet).split()) 

public_tweets = api.search('election')


print('Tweets')
for tweet in public_tweets:
    #print(tweet.text)
    u=tweet.text
    u=u.encode('unicode-escape').decode('utf-8')
   # v=v.encode('unicode-escape').decode('utf-8')
    
    print(u)
    
    #analysis = TextBlob(tweet.text)
    #print(analysis.sentiment)
print('created time')
for tweet in public_tweets:
    v=tweet.created_at
    print(v)
    
tweets_data_path=r'C:\Users\Rabin\dataafter3.json'

tweets_data=[]
tweets_file = open(tweets_data_path,"r")
for tweet in public_tweets:
    tweets_data.append(tweet.text)
    
    
