'''
Redis Handler URL Module
'''

from redis_handler import views
from django.urls import path

urlpatterns = [
    path('redis_pub_demo/', views.RedisPubDemo.as_view()),
]