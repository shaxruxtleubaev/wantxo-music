from django.contrib.admin import *
from .models import Song

@register(Song)
class SongAdmin(ModelAdmin):

    list_display = ('id', 'name', 'date',)
    list_display_links = ('name',)