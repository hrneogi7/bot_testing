from django.urls import path

from .views import index

urlpatterns=[path('chat',index,name='index')]