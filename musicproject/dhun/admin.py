from django.contrib import admin
from .models import Album,Song,Profile
# Register your models here.

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Profile)