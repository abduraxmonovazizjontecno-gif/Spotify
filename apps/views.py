from django.views.generic import TemplateView
from .models import Track, Category

from django.views.generic import TemplateView
from .models import Track, Category, Artist, Album


class MenuView(TemplateView):
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 1. Barcha qo'shiqlarni yuklanish vaqti bo'yicha saralab olamiz
        context['tracks'] = Track.objects.all().order_by('-created_at')

        # 2. Barcha artistlarni (ijrochilarni) olamiz
        context['artists'] = Artist.objects.all()

        # 3. Barcha albomlarni yangiligi bo'yicha olamiz
        context['albums'] = Album.objects.all().order_by('-created_at')

        # Sidebar-dagi kategoriyalar filtri uchun kerak bo'ladi
        context['categories'] = Category.objects.all()

        return context


class LoginView(TemplateView):
    template_name = 'login.html'


class RegisterView(TemplateView):
    template_name = 'register.html'


class FavouriteView(TemplateView):
    template_name = 'favourite.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tracks'] = Track.objects.all().order_by('-created_at')
        return context
