import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("FFweOVYTP8ZIQZylRAJGYYsqj")
    consumer_secret = os.getenv("4NAm2c0Dx0xkungOvQk08GqnEefp3Rm0X9eEPn4v5nN9AS84dk")
    access_token = os.getenv("fBAESZlGUuv12rqLFj8Lq0rROCRyokSRg0yrhSz9")
    access_token_secret = os.getenv("0pjlbzpoUw4i0nlmiWD8GFvnr8yT801dPR3gYiTzN424O")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api