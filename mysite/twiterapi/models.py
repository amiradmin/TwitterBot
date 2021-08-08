from django.db import models

# Create your models here.
class Mention(models.Model):
    tweetID = models.CharField(max_length=256, null=True, blank=True )
    accountName = models.CharField(max_length=256, null=True, blank=True )
    url = models.CharField(max_length=1024, null=True, blank=True )
    tweet = models.CharField(max_length=2048, null=True, blank=True )
    tweetDate = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.accountName