from umkm.models.profile import *
from django.contrib.auth.models import User
from umkm.utility import *


class Training(models.Model):
    TRAINING_TYPE = (('R', 'Request'), ('I', 'Information'), ('P', 'Proposal'))

    topic = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    venue = models.CharField(max_length=200)
    training_type = models.CharField(max_length=1, choices=TRAINING_TYPE)
    organizer = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.topic

    class Meta:
        verbose_name_plural = 'Pelatihan'
        verbose_name = 'Pelatihan'
        app_label = string_with_title("umkm", "Administrasi Pengetahuan")


class TrainingRO(Training):

    class Meta:
        proxy = True
        verbose_name_plural = 'Pelatihan'
        verbose_name = 'Pelatihan'
        app_label = string_with_title("umkm_display", "Manajemen Pengetahuan")