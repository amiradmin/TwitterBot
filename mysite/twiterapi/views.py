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
        menObj = Mention()
        twObj = Twitter()
        mentions=twObj.get_user_mentions_timeline()
        for mem in mentions:
            print(mem.text)
            if not Mention.objects.filter(tweetID = mem.id).first():
                menObj.tweetID = mem.id
                menObj.accountName = mem.user.screen_name
                menObj.tweetDate = mem.created_at
                menObj.tweet = mem.text


                for item in mem.entities['urls']:
                    menObj.url= item['expanded_url']
                    menObj.save()

        mention = Mention.objects.all()
        serializer = MentionSerializer(mention, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)