from django.urls import path
from . import views
urlpatterns = [
    path('', views.twitx, name='twitx'),
    path('home/', views.home, name='home'),
    path('like_unlike/', views.like_unlike, name='like_unlike')
]
