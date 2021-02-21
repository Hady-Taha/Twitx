from django.urls import path
from . import views
urlpatterns = [
    path('profile/<slug:slug>', views.profiles, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.authentication, name='login'),
    path('settings/<slug:slug>', views.settings, name='settings'),
    path('notification/<slug:slug>', views.notification, name='notification'),
    path('logout/', views.vlogout, name='logout'),
]
