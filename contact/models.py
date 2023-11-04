from django.db import models
from core.models import AbstractModel
# Create your models here.

class Message(AbstractModel):
    name = models.CharField(
        max_length=254,
        blank=True,
        verbose_name='Name',
    )
    email = models.EmailField(
        max_length=254,
        blank=True,
        verbose_name='Email',
    )
    subject = models.CharField(
        max_length=254,
        blank=True,
        verbose_name='Subject',
    )
    message = models.TextField(
        blank=True,
        verbose_name='Message',
    )

    def __str__(self):
        return f'Message: {self.name}'