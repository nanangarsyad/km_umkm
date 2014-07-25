from umkm.models.species import *
from django.contrib.auth.models import User
from umkm.utility import *


class Media(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    media_file = models.FileField(upload_to='file_upload/%Y/%m')
    creator = models.ForeignKey(User)
    shareable = models.BooleanField()

    def __unicode__(self):
        return self.title

    def image_thumb(self):
        return '<img src="/%s" width="100" height="100" />' % (self.media_file)
    image_thumb.allow_tags = True

    class Meta:
        verbose_name_plural = 'Gambar & File'
        verbose_name = 'Media'
        app_label = string_with_title("umkm", "Administrasi Pengetahuan")