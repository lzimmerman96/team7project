from django import forms
from .models import Artist, Artwork, Collection, Favorite, Rating, Tag


class UpdateArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('first_name', 'last_name', 'username', 'email', 'description', 'profile_picture')


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('user', 'artist_role', 'description', 'profile_picture')


class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ('artwork_title', 'artwork_description', 'artwork_artist', 'artwork_tag', 'artwork_picture')


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ('collection_name', 'collection_description', 'collection_artist', 'artwork')


class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ('favorite_artist', 'favorite_artwork')


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('rating_level', 'rating_artist', 'rating_artwork')


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('tag_name', 'tag_description')
