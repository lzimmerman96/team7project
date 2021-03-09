from . import views
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'gallery'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    re_path(r'^landing_page/$', views.landing_page, name='landing_page'),
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
    path('account_details', views.account_details, name='account_details'),
    path('account/<int:pk>/<int:pk_alt>/edit', views.update_account_details, name='update_account_details'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()