from django.db import models
from django.urls import reverse


class Phone(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False, auto_created=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=False)
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True, max_length=100, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('catalog', kwargs={'name_slug': self.slug})

    def __str__(self):
        return f'{self.name}, {self.price}, {self.release_date}'
