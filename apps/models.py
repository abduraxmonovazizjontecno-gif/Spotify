from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=255, verbose_name="Artist ismi")
    image = models.ImageField(upload_to='artists/', verbose_name="Artist rasmi (Dumaloq bo'ladi)")

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255, verbose_name="Albom nomi")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums', verbose_name="Albom muallifi")
    cover = models.ImageField(upload_to='albums/', verbose_name="Albom muqovasi (Rasm)")
    created_at = models.DateField(auto_now_add=True, verbose_name="Yaratilgan yili")

    def __str__(self):
        return self.title

class Track(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tracks', verbose_name="Kategoriyasi", null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name="Qo'shiq nomi")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='tracks', verbose_name="Ijrochi")
    icon = models.ImageField(upload_to='track_covers/', verbose_name="Qo'shiq rasmi", null=True, blank=True)
    audio_file = models.FileField(upload_to='tracks/', verbose_name="MP3 Fayl")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.artist.name} - {self.title}"

# MANA SEN SO'RAGAN ALBUM_TRACK MODELI!
class AlbumTrack(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_tracks', verbose_name="Albom")
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='album_tracks', verbose_name="Qo'shiq")
    order = models.PositiveIntegerField(default=0, verbose_name="Trek tartibi (Nomeri)")

    class Meta:
        ordering = ['order']
        verbose_name = "Albom qo'shig'i"
        verbose_name_plural = "Albom qo'shiqlari"

    def __str__(self):
        return f"{self.album.title} - {self.track.title}"