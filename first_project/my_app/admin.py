from django.contrib import admin

# Register your models here.

from .models import book
from .models import Director

admin.site.register(book)
admin.site.register(Director)

