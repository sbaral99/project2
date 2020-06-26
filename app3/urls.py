#path function
#we need views of app
#we need urlpattern list

from django.urls import path
from app3 import views

app_name='app3'

urlpatterns=[

    path('playing/',views.playing,name='playing'),

 
]