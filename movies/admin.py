from django.contrib import admin

from movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'genre', 'synopsis', 'release_date', 'created_at', 'modified_at', ]
