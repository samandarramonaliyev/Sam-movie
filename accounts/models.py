from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    is_anonymous = models.BooleanField(default=False)  # Foydalanuvchi anonim tanlagan bo'lsa True
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
