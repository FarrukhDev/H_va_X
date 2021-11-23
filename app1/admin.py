from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

@admin.register(Soz)
class SozAdmin(ModelAdmin):
    search_fields = ('soz',)

admin.site.register(Soz)
admin.site.register(N_soz)


# Register your models here.
