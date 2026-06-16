from django.views.generic import TemplateView
from .models import Track, Category

class MenuView(TemplateView):
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tracks'] = Track.objects.all().order_by('-created_at')

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