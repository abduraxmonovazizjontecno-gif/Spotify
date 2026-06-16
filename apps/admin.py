from django.contrib import admin
from .models import Category, Track

# Kategoriyalarni admin panelda ko'rsatish
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)} # Nomini yozganda slug avtomatik yoziladi

# Qo'shiqlarni admin panelda ko'rsatish
@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'category', 'icon', 'created_at') # Panelda ko'rinadigan ustunlar
    list_filter = ('category', 'artist') # O'ng tomondagi filter hisoblanadi
    search_fields = ('title', 'artist') # Qidiruv paneli