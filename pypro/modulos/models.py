from django.db import models


class Modulo(models.Model):
    titulo = models.CharField(max_length=64)
