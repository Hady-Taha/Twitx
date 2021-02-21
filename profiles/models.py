from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    firstName=models.CharField(max_length=50, blank=True, null=True)
    lastName=models.CharField(max_length=50, blank=True, null=True)
    photo=models.ImageField(upload_to='profilePhoto',default='photoEX.png')
    bio = models.TextField(max_length=100, blank=True, null=True)
    follow = models.ManyToManyField(User, related_name='follow', blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)
    
    def __str__(self):
        return str(self.user)
    @property
    def get_all_following(self):
        return self.sender.all()
    
    @property
    def get_all_following_count(self):
        return self.sender.all().count()

    @property
    def get_all_following_posts(self):
        qs = set()
        for i in self.sender.all():
            qs.add(i.receiver)
        return qs
    
    @property   
    def get_all_follower(self):
        return self.receiver.all()

    @property
    def get_all_follower_count(self):
        follower=0
        for followers in self.receiver.all():
            if followers.status == 'following':
                follower += 1
        return follower

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.user))
        super(Profile, self).save(*args, **kwargs)
        


class RelationShip(models.Model):
    STATUS_CHOICES = [('following', 'following'), ('UnFollow', 'UnFollow')]
    sender = models.ForeignKey(Profile, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, related_name='receiver', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(f'{self.sender} send to {self.receiver}')



class Notification(models.Model):
    NOTIFICATION_TYPES = (('Like', 'Like'), ('Comment', 'Comment'), ('Follow', 'Follow'))
    sender = models.ForeignKey(Profile, related_name='sender_notification', on_delete=models.CASCADE,blank=True, null=True)
    receiver = models.ForeignKey(Profile, related_name='receiver_notification', on_delete=models.CASCADE,blank=True, null=True)
    not_type = models.CharField(max_length=50, choices=NOTIFICATION_TYPES, blank=True, null=True)
    is_seen = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f'{self.sender} send to {self.receiver} {self.not_type}')
    
    




#https://www.youtube.com/watch?v=z4USlooVXG0&list=PLLRM7ROnmA9F2vBXypzzplFjcHUaKWWP5&index=1&ab_channel=JustDjango
#TODO:
# 1- Make modal to following [/]
# 2-  Notification [/]
# 3- Function to update profie (setting) [/] 
# 4- Posts app [/]
# 5- Comment []
# 6- Like [/]
