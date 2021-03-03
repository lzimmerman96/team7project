from django.shortcuts import render
from .models import *
from .forms import *
from django.utils import timezone

now = timezone.now()


def home(request):
    return render(request, 'gallery/home.html',
                  {'gallery': home})


def artwork_list(request):
    artwork = Artwork.objects.all()
    print(artwork)
    return render(request, 'gallery/artwork_list.html',
                  {'artworks': artwork})
