from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'gallery'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('artist_list', views.artist_list, name='artist_list'),
    path('artist/create/', views.artist_new, name='artist_new'),
    path('artist/<int:pk>/edit/', views.artist_edit, name='artist_edit'),
    path('artist/<int:pk>/delete/', views.artist_delete, name='artist_delete'),
    path('artwork_list', views.artwork_list, name='artwork_list'),
    path('artwork_list', views.artwork_list, name='collection_list'),
    path('artwork_list', views.artwork_list, name='favorite_list'),
    path('artwork_list', views.artwork_list, name='rating_list'),
    path('artwork_list', views.artwork_list, name='tag_list'),
    path('create_account', views.create_account, name='create_account'),
    path('account/<int:pk>/edit/', views.update_account_details, name='update_account_details'),
    # path('update_account_details', views.update_account_details, name='update_account_details')
]