from django.urls import path, include
from .views import *

app_name = 'blog'

urlpatterns = [
    path('news/', post_list, name='post_list')
]