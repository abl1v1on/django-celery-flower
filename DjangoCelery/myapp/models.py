from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(max_length=60, verbose_name='Почта')

    def __str__(self):
        return self.name
    