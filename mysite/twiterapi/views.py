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
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):

        twObj = Twitter()
        mentions=twObj.get_user_mentions_timeline()
        for mem in mentions:
            menObj = Mention()
            print("Here:"+mem.in_reply_to_status_id_str)
            print(mem.in_reply_to_screen_name)

            # menObj.accountName = mem.in_reply_to_screen_name
            # menObj.tweetID = mem.in_reply_to_status_id
            # menObj.tweet = mem.text
            # menObj.tweetDate = mem.created_at



            # menObj.tweet = tweet.text
            # menObj.tweetID = tweet.id_str

            if not Mention.objects.filter(tweetID = mem.in_reply_to_status_id).first():
                tweet = twObj.get_tweet_by_id(mem.in_reply_to_status_id_str)
                menObj.tweetID = mem.in_reply_to_status_id
                menObj.accountName = mem.in_reply_to_screen_name

                # menObj.tweetDate = tweet.created_at
                menObj.tweet = tweet.full_text
                # menObj.imageUrl = tweet.user.profile_image_url
                menObj.followers =int(tweet.user.followers_count)
                menObj.name = tweet.user.name
                menObj.description =  tweet.user.description
                menObj.avatarUrl =  tweet.user.profile_image_url_https

                menObj.following = twObj.get_following(tweet.user.id)
                print(tweet.user.id)
                print('========================')
                print()
                # print(tweet)
                if 'media' in tweet.entities:
                    for image in tweet.entities['media']:
                        print(image['media_url'])
                        menObj.imageUrl= image['media_url']

                for item in tweet.entities['urls']:
                    menObj.url = item['expanded_url']
                    # print(item['followers_count'])
                    # menObj.url = item['url']
                    # print( item['profile_image_url'])

                menObj.save()
            # print(tweet)




        mention = Mention.objects.all()
        serializer = MentionSerializer(mention, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


