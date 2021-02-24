from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Artist


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


# Registrations
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
