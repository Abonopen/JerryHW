from django.contrib import admin

# Register your models here.
from .models import Bookshops,Books

admin.site.register(Books)
admin.site.register(Bookshops)