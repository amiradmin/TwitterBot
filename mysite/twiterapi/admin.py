from django.contrib import admin
from twiterapi.models import Mention
# Register your models here.
class MentionAdmin(admin.ModelAdmin):
    list_display = ['id', 'accountName','tweetID', 'imageUrl','url','tweet', 'created_at', 'updated_at']
    list_filter = ['id', 'accountName', 'url','tweet', 'created_at', 'updated_at']

admin.site.register(Mention, MentionAdmin)