from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


# 1. ARTISTLAR (IJROCHILAR) MODELI
class Artist(models.Model):
    name = models.CharField(max_length=255, verbose_name="Artist ismi")
    image = models.ImageField(upload_to='artists/', verbose_name="Artist rasmi (Dumaloq bo'ladi)")

    def __str__(self):
        return self.name


# 2. ALBOMAR MODELI
class Album(models.Model):
    title = models.CharField(max_length=255, verbose_name="Albom nomi")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums', verbose_name="Albom muallifi")
    cover = models.ImageField(upload_to='albums/', verbose_name="Albom muqovasi (Rasm)")
    created_at = models.DateField(auto_now_add=True, verbose_name="Yaratilgan yili")

    def __str__(self):
        return self.title


# 3. QO'SHIQLAR MODELI (Senda bor edi, rasm maydoni va artist bog'liqligi qo'shildi)
class Track(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tracks', verbose_name="Kategoriyasi",
                                 null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name="Qo'shiq nomi")

    # Bu yerda shunchaki yozuv emas, tepada ochgan Artist modelimizga bog'lasak zo'r bo'ladi
    artist = models.CharField(max_length=255, verbose_name="Ijrochi (Matn shaklida)")

    # MANA SEN SIKYAPGAN RASM JOYI (Eski html kodimizdagi icon shu yerga ulanadi)
    icon = models.ImageField(upload_to='track_covers/', verbose_name="Qo'shiq rasmi", null=True, blank=True)

    audio_file = models.FileField(upload_to='tracks/', verbose_name="MP3 Fayl")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.artist} - {self.title}"