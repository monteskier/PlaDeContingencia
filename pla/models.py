from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Servei(models.Model):
    nomServei = models.CharField(max_length=50)
    CRITICITAT_CHOICES = (
        ('Baixa','Baixa'),
        ('Mitjana','Mitjana'),
        ('Alta','Alta'),
    )
    criticitat = models.CharField(max_length = 10, choices = CRITICITAT_CHOICES, default='Baixa')

    def __str__(self):
        return str(self.nomServei)

class Actiu(models.Model):
    nomActiu = models.CharField(max_length=50);
    descripcio = models.CharField(max_length=200);
    data_creacio = models.DateTimeField(auto_now = True, null=True, blank=True);
    data_error = models.DateTimeField(null=True, blank=True);
    ESTAT_CHOICES = (
        ('Operatiu','Operatiu'),
        ('Inoperatiu','Inoperatiu'),
    )
    estat = models.CharField(max_length = 25, choices = ESTAT_CHOICES, default = 'Operatiu')
    servei = models.ManyToManyField(Servei);

    def __str__(self):
        return str(self.nomActiu)

class Seguiment(models.Model):
    data_creacio = models.DateTimeField(auto_now = True)
    descripcio = models.CharField(max_length=250)
    actiu = models.ForeignKey(Actiu, on_delete = models.CASCADE)
    servei = models.ForeignKey(Servei, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.data_creacio)
