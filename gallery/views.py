from django.shortcuts import render
from .models import *
from .forms import *
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

now = timezone.now()


def landing_page(request):
    return render(request, 'gallery/landing_page.html',
                  {'gallery': landing_page})


def home(request):
    return render(request, 'gallery/home.html',
                  {'gallery': home})


# if account is created successfully, user will be automatically logged in and redirected to home page
def create_account(request):
    if request.method == "POST":
        user_form = CreateUserAccountForm(request.POST)
        artist_form = CreateArtistAccountForm(request.POST)
        if user_form.is_valid() and artist_form.is_valid():
            newuser = user_form.save()
            artist = artist_form.save(commit=False)
            artist.user = newuser
            artist.save()
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('gallery:home')
    else:
        user_form = CreateUserAccountForm()
        artist_form = CreateArtistAccountForm
    return render(request, 'registration/create_account.html',
                  {'user_form': user_form, 'artist_form': artist_form})


def account_details(request):
    return render(request, 'registration/account_details.html',
                  {'registration': account_details})


def update_account_details(request, pk, pk_alt):
    user_account = get_object_or_404(User, pk=pk)
    artist_account = get_object_or_404(Artist, pk=pk_alt)
    if request.method == "POST":
        # update
        user_form = UpdateUserForm(request.POST, instance=user_account)
        artist_form = UpdateArtistForm(request.POST, instance=artist_account)
        if user_form.is_valid() and artist_form.is_valid():
            user_account = user_form.save(commit=False)
            artist_account = artist_form.save(commit=False)
            user_account.updated_date = artist_account.updated_date = timezone.now()
            user_account.save()
            artist_account.save()
            return redirect('gallery:account_details')
    else:
        # edit
        user_form = UpdateUserForm(instance=user_account)
        artist_form = UpdateArtistForm(instance=artist_account)
    return render(request, 'registration/update_account_details.html', {
        'user_form': user_form,
        'artist_form': artist_form
    })


def artist_list(request):
    artist = Artist.objects.all()
    return render(request, 'gallery/artist_list.html',
                  {'artists': artist})


def artist_new(request):
    if request.method == "POST":
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.created_date = timezone.now()
            artist.save()
            return redirect('gallery:artist_list')
    else:
        form = ArtistForm()
        # print("Else")
    return render(request, 'gallery/artist_new.html', {'form': form})


def artist_edit(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == "POST":
        # update
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.updated_date = timezone.now()
            artist.save()
            return redirect('gallery:artist_list')
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
