from rest_framework import serializers



class MentionSerializer(serializers.Serializer):

    accountName = serializers.CharField(required=False, allow_blank=True, max_length=256)
    url = serializers.CharField(required=False, allow_blank=True, max_length=1024)
    tweet = serializers.CharField(required=False, allow_blank=True, max_length=2048)
