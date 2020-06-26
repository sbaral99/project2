#path function
#we need views of app
#we need urlpattern list

from django.urls import path
from app2 import views

app_name='app2'

urlpatterns=[

    path('read/',views.Read,name='read'),
    path('write/',views.Write,name='write'),


] 