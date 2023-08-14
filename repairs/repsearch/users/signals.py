from django.db.models.signals import post_save, post_delete  # или использовать декоратор:
from django.dispatch import receiver  # receiver используется как декоратор
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()

# post_save.connect(profile_update, sender=Profile)
# post_delete.connect(delete_user, sender=Profile)

















