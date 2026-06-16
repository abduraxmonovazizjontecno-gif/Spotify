from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    slug = models.SlugField(unique=True, blank=True, null=True) # URL yoki filterlar uchun

    def __str__(self):
        return self.name

class Track(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tracks', verbose_name="Kategoriyasi", null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name="Qo'shiq nomi")
    artist = models.CharField(max_length=255, verbose_name="Ijrochi")
    icon = models.CharField(max_length=10, default="🎵", verbose_name="Emodji/Ikonka")
    audio_file = models.FileField(upload_to='tracks/', verbose_name="MP3 Fayl")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.artist} - {self.title}"