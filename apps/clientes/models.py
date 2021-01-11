from django.db import models
from django.urls import reverse

# Create your models here.

class Cliente(models.Model):

  nome = models.CharField(max_length=254, verbose_name="Nome")
  endereco = models.CharField(max_length=254, verbose_name="Endereço")
  numero = models.CharField(max_length=10, verbose_name="Numero")
  complemento = models.CharField(max_length=50, verbose_name="Complemento",blank=True)
  bairro = models.CharField(max_length=50, verbose_name="Bairro")
  cidade = models.CharField(max_length=254, verbose_name="Cidade")
  uf = models.CharField(max_length=2, verbose_name="UF")
  telefone = models.CharField(max_length=19, verbose_name="Fixo",blank=True)
  celular = models.CharField(max_length=19, verbose_name="Celular",blank=True)
  rg = models.CharField(max_length=15, verbose_name="RG")
  cpf = models.CharField(max_length=15, verbose_name="CPF")
  data_nascimento = models.DateField(verbose_name="Data de Nascimento")
  email = models.EmailField(max_length=254, verbose_name="E-mail")

  class Meta:
    verbose_name = 'Cliente'
    verbose_name_plural = 'Clientes'

  def __str__(self):
    return self.nome

  def get_absolute_url(self):
    return reverse("cliente__detail", kwargs={"pk": self.pk})

  def get_update_url(self):
    return reverse("cliente__atualiza", kwargs={"pk": self.pk})

  def get_delete_url(self):
    return reverse("cliente__delete", kwargs={"pk": self.pk})
