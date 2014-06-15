from django.db import models
from umkm.models.species import *
from umkm.models.profile import Profile
from django.contrib.auth.models import User


class Media(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    creator = models.ForeignKey(User)
    media_type = models.ForeignKey(Type)
    shareable = models.BooleanField()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'List Media'
        verbose_name = 'Media'
        app_label = 'umkm'