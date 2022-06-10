from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from recipe.models import User


class Profile(models.Model):
    """
    Class for the profile model
    1:1 - User model (user)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """
        Automatically creates a profile object linked to
        the user when a user is created
        """
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        """
        Saves the profile when the user is saved
        """
        instance.profile.save()
