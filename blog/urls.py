from django.urls import path
from . import views,include

urlpatterns = [
path('', views.post_list, name='post_list'),
]
