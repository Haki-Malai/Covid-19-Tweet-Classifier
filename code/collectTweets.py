import tweepy

api_key = "*****"
api_secret = "*****"
access_token = "*****"
access_token_secret = "*****"
#create authentication for accessing Twitter
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

#initialize Tweepy API
api = tweepy.API(auth)

HASHTAGS = '#covid-19'
ITEMS = 2000
e = 1
for tweet in tweepy.Cursor(api.search, q=HASHTAGS+' -filter:retweets', \
                                lang="en", tweet_mode='extended').items(ITEMS):
    file = open('Neural Networks/myTweet' + str(e) + '.txt', 'a', encoding="UTF-8")
    file.write(str([tweet.full_text.replace('\n',' ').encode('utf-8')]))
    e = e + 1
print("Tweet Collection Complete")
