import tweepy

class Twitter():
    """This class manipulate Tittwer API """
    userID = None   #Target Twitter user id
    def __init__(self):
        self.auth = tweepy.OAuthHandler('BEKlyQhmhfBJ4MWtgHu6lKZ90', 'PPhCfYZvYwKSzNkowSEQ2K2FEHR54wejU8WNqILlKKp79Dgbjj')
        self.auth.set_access_token('959812651-uYaji4Ibc7hxJiGs7g8HtovLeNbb91U0P51yjlFE', '567d5wjaIzy8RerGpAjNfDoSDjiVeseLzvtlpF7j2bgZw')
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
        self.userID = 'UrlTestBot'

    def get_followers(self):
        for follower in self.api.followers(self.userID):
            print(follower.screen_name)
            # return follower.screen_name


    def get_following(self,id):
        user = self.api.get_user(id)
        return user.friends_count

    def get_user_home_timeline(self):
        public_tweets = self.api.home_timeline()[:1]
        for tweet in public_tweets:
            print(tweet)

    def get_user_mentions_timeline(self):
        mentions = self.api.mentions_timeline()[:]
        # for men in mentions:
        #     print(men.user.screen_name)
        #     for item in men.entities['urls']:
        #         print(item['expanded_url'])
        return mentions
    def get_tweet_by_id(self,tweetID):
        tweet = self.api.get_status(id=tweetID,tweet_mode='extended')
        return tweet

    def get_targt_user_timeline(self):
        tweets = self.api.user_timeline(screen_name=self.userID,
                                   # 200 is the maximum allowed count
                                   count=200,
                                   include_rts=False,
                                   # Necessary to keep full_text
                                   # otherwise only the first 140 words are extracted
                                   tweet_mode='extended'
                                   )
        for info in tweets[:3]:
            print("ID: {}".format(info.id))
            print(info.created_at)
            print(info.full_text)
            print("\n")
        return tweets

    def search(self,search_words, date_since):
        # Collect tweets
        tweets = tweepy.Cursor(self.api.search,
                               screen_name=self.userID,
                               q=search_words,
                               lang="en",
                               since=date_since).items(5)
        # Iterate and print tweets
        for tweet in tweets:
            print(tweet.text)


if __name__ == "__main__":
    obj = Twitter()
    # obj.get_followers()
    # obj.get_user_home_timeline()
    # obj.get_targt_user_timeline()
    # obj.search('einem',"2018-11-16")
    obj.get_user_mentions_timeline()