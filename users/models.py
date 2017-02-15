from django.db import models

from django.core.urlresolvers import reverse

from django.contrib.auth.models import User as DjangoUser


class User(DjangoUser):

    def get_absolute_url(self):

        return reverse('users-view', kwargs={'pk': self.id})


class Company(models.Model):
    name = models.CharField(max_length=255, )
    address = models.CharField(max_length=255,)
    email = models.EmailField(blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('contacts-view', kwargs={'pk': self.id})

    class Meta:
        unique_together = ('name', 'address',)

    def __str__(self):
        return ' '.join([self.name, self.address])