from django.db import models
from django.utils import timezone


class Oil(models.Model):
    name = models.TextField()
    sae = models.CharField(max_length=6)
    spec = models.TextField()
    package_size = models.CharField(max_length=4)


class Store(models.Model):
    name = models.CharField(max_length=25)
    url = models.CharField(max_length=255)


class Price(models.Model):
    oil_id = models.ForeignKey(Oil, on_delete=models.DO_NOTHING())
    store_id = models.ForeignKey(Store, on_delete=models.DO_NOTHING())
    data = models.DateTimeField(default=timezone.now)
    price = models.CharField(max_length=20)
