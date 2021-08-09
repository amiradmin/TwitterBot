from rest_framework import serializers



class MentionSerializer(serializers.Serializer):

    accountName = serializers.CharField(required=False, allow_blank=True, max_length=256)
    url = serializers.CharField(required=False, allow_blank=True, max_length=2048)
    imageUrl = serializers.CharField(required=False, allow_blank=True, max_length=2048)
    tweet = serializers.CharField(required=False, allow_blank=True, max_length=2048)
    name = serializers.CharField(required=False, allow_blank=True, max_length=2048)
    description = serializers.CharField(required=False, allow_blank=True, max_length=2048)
    avatarUrl = serializers.CharField(required=False, allow_blank=True, max_length=2048)
    followers = serializers.IntegerField(required=False)
