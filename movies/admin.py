from django.contrib import admin
from .models import Movie, Info, Comment

# Registering models

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title","year"]
    list_filter = ["year"]
    search_fields = ["title"]

admin.site.register(Info)
admin.site.register(Comment)

