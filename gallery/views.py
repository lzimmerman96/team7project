from django.shortcuts import render
from .models import *
from .forms import *
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect



now = timezone.now()


def home(request):
    return render(request, 'gallery/home.html',
                  {'gallery': home})


def artist_list(request):
    artist = Artist.objects.all()
    return render(request, 'gallery/artist_list.html',
                 {'artists': artist})


def artist_new(request):
   if request.method == "POST":
       form = ArtistForm(request.POST)
       if form.is_valid():
           artist = form.save(commit=False)
           artist.created_date = timezone.now()
           artist.save()
           artists = Artist.objects.all()
           return render(request, 'gallery/artist_list.html',
                         {'artists': artists})
   else:
       form = ArtistForm()
       # print("Else")
   return render(request, 'gallery/artist_new.html', {'form': form})

def artist_edit(request, pk):
   artist = get_object_or_404(Artist, pk=pk)
   if request.method == "POST":
       # update
       form = ArtistForm(request.POST, instance=artist)
       if form.is_valid():
           artist = form.save(commit=False)
           artist.updated_date = timezone.now()
           artist.save()
           artist = Artist.objects.all()
           return render(request, 'gallery/artist_list.html',
                         {'artists': artist})
   else:
        # edit
       form = ArtistForm(instance=artist)
   return render(request, 'gallery/artist_edit.html', {'form': form})

def artist_delete(request, pk):
   artist = get_object_or_404(Artist, pk=pk)
   artist.delete()
   return redirect('gallery:artist_list')

def artwork_list(request):
    artwork = Artwork.objects.all()
    print(artwork)
    return render(request, 'gallery/artwork_list.html',
                  {'artworks': artwork})
