from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel


class Modulo(OrderedModel):
    titulo = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    publico = models.TextField()
    descricao = models.TextField()

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('modulos:detalhe', kwargs={'slug': self.slug})
