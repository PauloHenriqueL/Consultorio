from django.contrib import admin
from . import models


class TerapeutaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'usuario', 'Decano')
    search_fields = ('nome',)

admin.site.register(models.Terapeuta, TerapeutaAdmin)
