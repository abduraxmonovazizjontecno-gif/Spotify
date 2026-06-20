from django.views.generic import TemplateView, DetailView
from .models import Track, Category, Artist, Album, AlbumTrack


class MenuView(TemplateView):
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tracks'] = Track.objects.all().order_by('-created_at')
        context['artists'] = Artist.objects.all()
        context['albums'] = Album.objects.all().order_by('-created_at')
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



class AlbumDetailView(DetailView):
    model = Album
    template_name = 'album-detail.html'
    context_object_name = 'album'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album_tracks'] = (
            AlbumTrack.objects.filter(album=self.object)
            .select_related('track', 'track__artist')
        )
        context['related_albums'] = (
            Album.objects.filter(artist=self.object.artist)
            .exclude(pk=self.object.pk)
            .order_by('-created_at')[:6]
        )
        context['more_albums'] = (
            Album.objects.exclude(pk=self.object.pk)
            .order_by('-created_at')[:8]
        )
        context['categories'] = Category.objects.all()
        return context