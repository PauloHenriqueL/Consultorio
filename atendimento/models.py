from django.db import models
from decano.models import Decano
from Terapeuta.models import Terapeuta
from pacientes.models import Paciente


class Atendimento(models.Model):  # Cria o model
    decano = models.ForeignKey(Decano, on_delete=models.PROTECT, related_name='atendimento')
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name='atendimento')
    Terapeuta = models.ForeignKey(Terapeuta, on_delete=models.PROTECT, related_name='atendimento')
    data = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)  # Insere um time quando cria o campo
    update_at = models.DateTimeField(auto_now=True)  # Insere um time quando edita o campo

    class Meta:  # Ordene por name
        ordering = ['paciente']

    def __str__(self):  # Cite o objeto dele pelo name
        return self.paciente.nome
