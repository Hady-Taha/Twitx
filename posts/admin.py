from django.contrib import admin
from .models import Post, Like
# Register your models here.
admin.site.register(Post)
admin.site.register(Like)


# {% for post in request.user.profile.get_all_following %}
#     {% for posts in post.receiver.user_post.all %}
#         <p>{{posts}}</p>
#     {% endfor %}
# {% endfor %}