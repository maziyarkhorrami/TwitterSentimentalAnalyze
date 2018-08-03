import tweepy
from textblob import TextBlob
from pandas import DataFrame

consumer_key = 'CONSUMER_TOKEN_FROM_TWEETER_DEVELOPER'
consumer_secret = 'CONSUMER_SECRET_FROM_TWEETER_DEVELOPER'

access_token = 'ACCESS_TOKEN_FROM_TWEETER_DEVELOPER'
access_token_secret = 'ACCESS_TOKEN_SECRET_FROM_TWEETER_DEVELOPER'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('MacBook')

list_of_dict = []

for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    if analysis.sentiment[0] > 0.0:
        data = {'Tweet': tweet.text, 'Pos/Neg': 'pos'}
    if analysis.sentiment[0] <= 0.0:
        data = {'Tweet': tweet.text, 'Pos/Neg': 'neg'}

    list_of_dict.append(data)

df = DataFrame(data=list_of_dict, columns=['Tweet', 'Pos/Neg'])
df.to_csv('sentimental_analyze_macbook.csv', index='True', header='True')
print(df)