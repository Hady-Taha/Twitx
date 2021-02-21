from django.contrib import admin
from .models import Profile, RelationShip, Notification
# Register your models here.
admin.site.register(Profile)
admin.site.register(RelationShip)
admin.site.register(Notification)
