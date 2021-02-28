from django import forms
from django.contrib.auth.models import Artist


class ArtistDeleteForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = []   #Form has only submit button.  Empty "fields" list still necessary, though.