from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


""" The receiver receives the signal and performs the actions"""

#how do we fire this function -> we add a receiver as  a decorator this particular function

@receiver(post_save,sender=User)
def build_profile(sender,instance,created,**kwargs):
    #check if user has been created 
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

    