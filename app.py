import tweepy

auth = tweepy.OAuthHandler('FFweOVYTP8ZIQZylRAJGYYsqj', '4NAm2c0Dx0xkungOvQk08GqnEefp3Rm0X9eEPn4v5nN9AS84dk')
auth.set_access_token('959812651-fBAESZlGUuv12rqLFj8Lq0rROCRyokSRg0yrhSz9', '0pjlbzpoUw4i0nlmiWD8GFvnr8yT801dPR3gYiTzN424O')
api = tweepy.API(auth)

public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
id='save_video'
# user = api.get_user('save_video')
# print(user.screen_name)

# api.user_timeline(id="save_video")
# for status in tweepy.Cursor(api.user_timeline).items():
#     # process status here
#     process_status(status)

# for page in tweepy.Cursor(api.user_timeline).items():
#     # page is a list of statuses
#     print(page.text)

# tweet = api.user_timeline(id=id, count=5)[0]
# print(tweet.text)
#
tweets = api.user_timeline(screen_name=id,
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
for info in tweets[:]:
     print("ID: {}".format(info.id))
     print(info.created_at)
     print(info.full_text)
     print("\n")
#
# public_tweets = api.home_timeline(screen_name=id)
# for tweet in public_tweets:
#     print(tweet.text)

# for status in tweepy.Cursor(api.user_timeline, screen_name='@save_video', tweet_mode="extended").items(3):
#     print(status.full_text)


search_words = "download"
date_since = "2018-11-16"

# Collect tweets
tweets = tweepy.Cursor(api.search,
                   q=search_words,
                   lang="en",
                   since=date_since).items(5)

# Iterate and print tweets
# for tweet in tweets:
#     print(tweet.text)


for follower in api.followers(id):
    print(follower.screen_name)

def get_last_tweet(self):
    tweet = api.user_timeline(id = id, count = 1)[0]
    print(tweet.text)