from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile,RelationShip,Notification
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def post_save_create_profile(sender, created, instance, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=RelationShip)
def post_save_RelationShip(sender, created, instance, *args, **kwargs):
    sender_ = instance.sender
    receiver_ = instance.receiver
    
    if instance.status == 'following':
        sender_.follow.add(receiver_.user)
        get, created = Notification.objects.get_or_create(sender=sender_, receiver=receiver_, not_type='Follow' , is_seen=False)
        receiver_.save()
        sender_.save()


    elif instance.status == 'UnFollowing':
        receiver_.follow.remove(sender_.user)
        receiver_.save()
        sender_.save()
