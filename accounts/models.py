from django.contrib.auth.models import User
from django.db import models  # noqa


class Profile(models.Model):
    user = models.OneToOneField(
        to='auth.User',
        on_delete=models.CASCADE,
        related_name='profile'
    )
    image = models.ImageField(
        null=True,
        default='default.jpg',
        upload_to='pics/',
        blank=True
    )


# @classmethod
# def generate_profiles(self):
#     for user in User.objects.all():
#         try:
#             user.profile
#         except:
#             profile = Profile()
#             profile.user = user
#             profile.save()
