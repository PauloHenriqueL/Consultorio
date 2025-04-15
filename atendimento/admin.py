from django.contrib import admin
from . import models


class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'Terapeuta', 'decano')
    search_fields = ('paciente',)

admin.site.register(models.Atendimento, AtendimentoAdmin)
