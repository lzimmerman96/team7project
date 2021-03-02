from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Artist, Artwork, Collection, Tag, Rating, Favorite


# Register your models here.

# This is so the changes made to the default User show up
# and are editable in the Admin's pov.

# "Define an inline admin descriptor for Artist model
# which acts a bit like a singleton"
class ArtistInline(admin.StackedInline):
    model = Artist
    can_delete = False  # this might change


# Define a new User Admin
class UserAdmin(BaseUserAdmin):
    inlines = (ArtistInline,)


# This is for adding multiple artists to one
# Artwork submission.
class ArtworkAdmin(admin.ModelAdmin):
    model = Artwork
    # filter_horizontal = ('artwork_artist', 'artwork_tag')
    filter_horizontal = ('artwork_tag',)


# This is for adding multiple pieces of Artwork
# to the Collection.
class CollectionAdmin(admin.ModelAdmin):
    model = Collection
    filter_horizontal = ('artwork',)


# This is for adding to pieces
# of Artwork.
class FavoriteAdmin(admin.ModelAdmin):
    model = Favorite
    filter_horizontal = ('favorite_artwork',)


# This for for displaying the Fields for Ratings.
class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating_artwork', 'rating_level', 'rating_artist')


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# Register other models
admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Tag)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Favorite, FavoriteAdmin)
