from django.contrib import admin
from .models import Category, Track, Artist, Album

# 1. Kategoriyalar uchun admin sozlamalari
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}  # Nomini yozganda slug avtomatik to'ladi


# 2. Artistlar (Ijrochilar) uchun admin sozlamalari
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')     # Ro'yxatda ID, Ismi va Rasmi ko'rinadi
    search_fields = ('name',)                  # Ismi bo'yicha qidirsa bo'ladi


# 3. Albomlar uchun admin sozlamalari
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'cover', 'created_at') # Ro'yxat ustunlari
    list_filter = ('artist',)                                       # Artist bo'yicha filter
    search_fields = ('title', 'artist__name')                       # Albom nomi bo'yicha qidiruv


# 4. Qo'shiqlar (Tracks) uchun admin sozlamalari
@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    # Endi 'icon' maydoni models.py da borligi uchun bu yerda error bermaydi!
    list_display = ('id', 'title', 'artist', 'category', 'icon', 'created_at')
    list_filter = ('category', 'artist')
    search_fields = ('title', 'artist')