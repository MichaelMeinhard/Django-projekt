from django.contrib import admin
from .models import Genre, Series, Director

# Register your models here.
admin.site.register(Genre)
admin.site.register(Series)
admin.site.register(Director)
