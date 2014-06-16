from django.db import models
from umkm.models.profile import Profile
from django.contrib.auth.models import User

class Training(models.Model):
    TRAINING_TYPE = (('R', 'Request'), ('I', 'Information'), ('P', 'Proposal'))

    topic = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    venue = models.CharField(max_length=200)
    training_type = models.CharField(max_length=1, choices=TRAINING_TYPE)
    organizer = models.ForeignKey(User)

    def __unicode__(self):
        return self.topic

    class Meta:
        verbose_name_plural = 'List Pelatihan'
        verbose_name = 'Pelatihan'
        app_label = 'umkm'