from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# Here we override the default User model
# to add more fields dedicated to that Artist.
# Django already has these fields included for users: id PK, password,
# is_superuser, username, last_name, email, is_staff, is_active, first_name

# These can be accessed like: u = User.objects.get(username='mayalanger')

# For more details:
# https://stackoverflow.com/questions/42478191/django-how-to-add-an-extra-field-in-user-model-and-have-it-displayed-in-the-adm/42481381
# https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#extending-the-existing-user-model
class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=280)  # this is the default for all descriptions

    # https://www.geeksforgeeks.org/python-uploading-images-in-django/

    # to user this, we need to install Pillow.  "python -m pip install Pillow" or
    # download it at https://pypi.org/project/Pillow/
    # "the Python Imaging Library adds image processing capabilities to your Python interpreter"
    #  - https://pypi.org/project/Pillow/
    # profile_picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.user}'


# Tags can be added to Artwork.
class Tag(models.Model):
    # tag_id is not needed as a field on this file.  It can be referenced by other models.
    tag_name = models.CharField(max_length=50)
    tag_description = models.TextField(max_length=280)

    def __str__(self):
        return f'{self.tag_name}'


# This is the Model representing a piece of Artwork (not specifically a submission of a piece)
class Artwork(models.Model):
    # artwork_id this is not needed as a field on this file.  It can be referenced by other models.
    artwork_title = models.CharField(max_length=200)
    artwork_description = models.TextField(max_length=280)
    # One piece of Artwork can have multiple Artists
    artwork_artist = models.ManyToManyField(Artist)
    # One piece of Artwork can have multiple Tags
    artwork_tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.artwork_title}'


# Each Collection has many pieces of Artwork inside it.  A Collection is
# created by one User.
class Collection(models.Model):
    # collection_id is not needed as a field on this file.  It can be referenced by other models.
    collection_name = models.CharField(max_length=200)
    collection_description = models.TextField(max_length=280)
    # this collection will cease to exist when an Artist deletes their account.
    collection_artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    # this collection will have many pieces of Artwork inside it.
    artwork = models.ManyToManyField(Artwork)

    def __str__(self):
        return f'{self.collection_name}'
