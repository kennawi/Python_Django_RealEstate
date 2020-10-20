from django.db import models

# Create your models here.
from django.db import models


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(max_length=400)

    def __str__(self):
        return self.name
