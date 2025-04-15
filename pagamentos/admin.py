from django.contrib import admin
from . import models


class PagamentosAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'Data', 'Atendimento')
    search_fields = ('paciente',)

admin.site.register(models.Pagamento, PagamentosAdmin)
