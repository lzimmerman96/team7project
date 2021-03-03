from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'gallery'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('artwork_list', views.artwork_list, name='artist_list'),
    path('artwork_list', views.artwork_list, name='artwork_list'),
    path('artwork_list', views.artwork_list, name='collection_list'),
    path('artwork_list', views.artwork_list, name='favorite_list'),
    path('artwork_list', views.artwork_list, name='rating_list'),
    path('artwork_list', views.artwork_list, name='tag_list'),
]