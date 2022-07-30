from django.contrib import admin

# Register your models here.
from album.models import City, Genre, Album, Song


admin.site.register(City)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Song)