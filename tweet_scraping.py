import snscrape.modules.twitter as sntwitter
import pandas as pd
#from textblob import TextBlob


# query_params = {'query':'place:California place_country:ID has:geo -is:retweet',
#                 #'max_results':'500',
#                 'start_time':'2010-01-01T00:00:00Z',
#                 'expansions': 'geo.place_id,author_id',
#                 'tweet.fields': 'id,text,author_id,created_at,geo,lang',
#                 'user.fields': 'id,name,username,created_at,description,location',
#                 'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
#                'next_token': {}}

query = "(from:elonmusk) lang:en since:2017-01-01 until:2021-12-30"
tweets = []
limit = 1000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        # lang = TextBlob(tweet.content)
        # print(tweet);
        tweets.append([tweet.date, tweet.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])

# to save to csv
df.to_csv('IK_tweets_ur.csv', encoding='utf_8_sig')