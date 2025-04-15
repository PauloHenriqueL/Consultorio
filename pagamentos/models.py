from django.db import models
from pacientes.models import Paciente
from atendimento.models import Atendimento


class Pagamento(models.Model):  # Cria o model
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name='pagamento')
    Data = models.DateTimeField()
    Atendimento = models.ForeignKey(Atendimento, on_delete=models.PROTECT, related_name='pagamento')
    created_at = models.DateTimeField(auto_now_add=True)  # Insere um time quando cria o campo
    update_at = models.DateTimeField(auto_now=True)  # Insere um time quando edita o campo

    class Meta:  # Ordene por name
        ordering = ['paciente']

    def __str__(self):  # Cite o objeto dele pelo name
        return self.paciente.nome
