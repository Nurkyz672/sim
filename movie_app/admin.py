from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(MovieVideo)


