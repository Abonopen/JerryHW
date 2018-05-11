from django.contrib import admin

# Register your models here.
from .models import Myself,member

admin.site.register(member)
admin.site.register(Myself)