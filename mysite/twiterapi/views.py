from django.shortcuts import render
from twiterapi.serializers import MentionSerializer
from twiterapi.models import  Mention
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from classes.designTwitter import Twitter

class MentionList(APIView):
    """
        This class get content of a tweet if someone mentions my account
    """

    def get(self, request, format=None):

        twObj = Twitter()
        mentions=twObj.get_user_mentions_timeline()
        for mem in mentions:
            menObj = Mention()
            print("Here:"+mem.in_reply_to_status_id_str)
            print(mem.in_reply_to_screen_name)
            reply = twObj.get_tweet_by_id(mem.id)
            print(reply.full_text)

            keywords = ["save", "Save", "SAVE"]
            result = any(keyword in reply.full_text for keyword in keywords)
            if result:
                print(result)
                if not  Mention.objects.filter(tweetID = mem.in_reply_to_status_id).first():
                    tweet = twObj.get_tweet_by_id(mem.in_reply_to_status_id_str)
                    menObj.tweetID = mem.in_reply_to_status_id
                    menObj.accountName = mem.in_reply_to_screen_name
                    print(mem.id)
                    menObj.tweet = tweet.full_text
                    menObj.followers =int(tweet.user.followers_count)
                    menObj.name = tweet.user.name
                    menObj.description =  tweet.user.description
                    menObj.avatarUrl =  tweet.user.profile_image_url_https

                    menObj.following = twObj.get_following(tweet.user.id)
                    # print(tweet)
                    if 'media' in tweet.entities:
                        for image in tweet.entities['media']:
                            print(image['media_url'])
                            menObj.imageUrl= image['media_url']

                    for item in tweet.entities['urls']:
                        menObj.url = item['expanded_url']

                    menObj.save()





        mention = Mention.objects.all()
        serializer = MentionSerializer(mention, many=True)
        return Response(serializer.data)
