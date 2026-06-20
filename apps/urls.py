from django.urls import path
from .views import MenuView, LoginView, RegisterView, FavouriteView,AlbumDetailView


urlpatterns = [
    path('', MenuView.as_view(), name='menu'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('favourite/', FavouriteView.as_view(), name='favourite'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
]