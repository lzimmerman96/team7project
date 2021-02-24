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
