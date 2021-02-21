from .models import Notification , Profile
from django.shortcuts import redirect


def noteF(request):
    if request.user.is_authenticated == False or request.user.username != request.user.profile.slug:
        return {'data':False}
    profile = Profile.objects.get(slug=request.user.profile.slug)
    not_f = Notification.objects.filter(receiver=profile,is_seen=False)
    return {'not_f': not_f}
