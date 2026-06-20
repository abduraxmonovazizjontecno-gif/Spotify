from django.contrib import admin
from .models import Category, Artist, Album, Track, AlbumTrack

# Albom yaratayotganda uning ichida qo'shiqlarni tartibi bilan bir marta qo'shish imkoniyati (Inline)
class AlbumTrackInline(admin.TabularInline):
    model = AlbumTrack
    extra = 1  # Boshida nechta bo'sh qator ko'rinishi
    autocomplete_fields = ['track']  # Treklar ko'p bo'lsa qidiruv bilan oson topish uchun


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
    search_fields = ('title', 'artist__name')                       # Albom nomi yoki artist ismi bo'yicha qidiruv
    inlines = [AlbumTrackInline]  # 🎯 Mana shu joyi albom ichida treklarni navbat bilan chiqarib beradi!


# 4. Qo'shiqlar (Tracks) uchun admin sozlamalari
@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'category', 'icon', 'created_at')
    list_filter = ('category', 'artist')
    search_fields = ('title', 'artist__name')  # 💡 artist matn bo'lmagani uchun artist__name deb qidiramiz


# 5. Albom va Trek munosabati uchun alohida admin sozlamasi (ixtiyoriy lekin foydali)
@admin.register(AlbumTrack)
class AlbumTrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'album', 'track', 'order')
    list_editable = ('order',)  # Tartib raqamini ro'yxatning o'zidan turib o'zgartirish
    list_filter = ('album',)