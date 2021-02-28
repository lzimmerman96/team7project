from django.shortcuts import render

now = timezone.now()
def home(request):
   return render(request, 'crm/home.html',
                 {'crm': home})

# Create your views here.
@login_required
def delete_artist(request):
    if request.method == 'POST':
        delete_form = ArtistDeleteForm(request.POST, instance=request.user)
        artist = request.artist
        artist.delete()
        messages.info(request, 'Your account has been deleted.')
        return redirect('blog-home')
    else:
        delete_form = ArtistDeleteForm(instance=request.artist)

    context = {
        'delete_form': delete_form
    }

    return render(request, 'users/delete_form.html', context)
