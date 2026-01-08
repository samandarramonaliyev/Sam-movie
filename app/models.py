from django.db import models
from PIL import Image
from django.contrib.auth.models import User

class Janr(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Film(models.Model):
    image = models.ImageField(upload_to='film_image/', null=True, blank=True)
    name = models.CharField(max_length=155)
    description = models.TextField(null=True)
    direct_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    actor = models.TextField(null=True)
    duration = models.CharField(max_length=20)
    genres = models.ManyToManyField(
        Janr,
        related_name="admin_films",
        blank=True
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    approved = models.BooleanField(default=False)
    anonymous = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name}; {self.direct_by}; {self.duration}"
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            try:
                img = Image.open(self.image.path)
                target_size = (400, 600)
                img = img.resize(target_size, Image.LANCZOS)
                img.save(self.image.path)
            except Exception:
                # serverda yoki developda media fayl yo'qligida xato chiqmasligi uchun pass
                pass


# class Category(models.Model):
#     film = models.ForeignKey(Film, on_delete=models.CASCADE, null=True, blank=True)
#     # user_film = models.ForeignKey(UserFilm, on_delete=models.CASCADE, null=True, blank=True)
#     janr = models.ForeignKey(Janr, on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return f"{self.film}: {self.janr}"