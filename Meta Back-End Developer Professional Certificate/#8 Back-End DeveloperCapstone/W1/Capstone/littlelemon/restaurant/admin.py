from . import models
from django.contrib import admin
from rest_framework.authtoken.models import Token

admin.site.register(models.Menu)
admin.site.register(models.MenuItem)
admin.site.register(models.Booking)
admin.site.register(Token)
