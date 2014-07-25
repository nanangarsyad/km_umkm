from django.db import models
from umkm.utility import *


class Category(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, default=None)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Kategori'
        verbose_name = 'Kategori'
        app_label = string_with_title("umkm", "Administrasi Pengetahuan")


# class Type(models.Model):
#     FOR_TYPE = (('K', 'Knowledge'), ('R', 'Relation'), ('M', 'Media'), ('P', 'Profile'))
#
#     title = models.CharField(max_length=200)
#     type_for = models.CharField(max_length=1, choices=FOR_TYPE)
#     creator = models.ForeignKey(User)
#
#     def __unicode__(self):
#         return self.title
#
#     class Meta:
#         verbose_name_plural = 'Tipe'
#         verbose_name = 'Tipe'
#         app_label = 'umkm'


class Tag(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Label'
        verbose_name = 'Label'
        app_label = string_with_title("umkm", "Administrasi Pengetahuan")