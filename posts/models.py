from django.db import models
from profiles.models import Profile
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(Profile, related_name='user_post', on_delete=models.CASCADE)
    liked = models.ManyToManyField(Profile, blank=True, null=True)
    body = models.TextField(max_length=750)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_all_likes_count(self):
        return self.liked.all().count()

    def get_all_likes(self):
        return self.liked.all()

    def __str__(self):
        return str(f'{self.user} post {self.body[:20]}')

    



class Like(models.Model):
    VALUE_CHOICES = [('Like', 'Like'), ('UnLike', 'UnLike')]
    user = models.ForeignKey(Profile, related_name='user_like', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_like', on_delete=models.CASCADE)
    value = models.CharField(max_length=50, choices=VALUE_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(f'{self.user} liked {self.post}')
