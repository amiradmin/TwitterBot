from django.urls import path,include
from twiterapi import views
from django.conf import settings



app_name ="twiterapi"
urlpatterns = [


  
    path('mentions/', views.MentionList.as_view(), name='mentions_'),


]
