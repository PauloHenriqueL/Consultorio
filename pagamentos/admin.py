from django.contrib import admin
from .models import Pagamento


class PagamentosAdmin(admin.ModelAdmin):
    # Exibe os campos no painel de administração
    list_display = ('paciente', 'Data', 'Atendimento')
    # Permite busca pelos campos especificados
    search_fields = ('paciente',)


# Registra o modelo Pagamento no painel de administração
admin.site.register(Pagamento, PagamentosAdmin)
