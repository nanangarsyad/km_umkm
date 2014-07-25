from umkm.models.species import *
from django.contrib.auth.models import User
from umkm.utility import *


class Profile(models.Model):
    USER_TYPES = (
    ('1', 'Administrator'),
    ('2', 'UMKM'),
    ('3', 'Researcher'),
    ('4', 'Lainnya'),
    )

    user = models.OneToOneField(User)
    user_type = models.CharField(max_length=1, choices=USER_TYPES)
    address = models.CharField(max_length=200)
    instance_name = models.CharField(max_length=200)
    instance_desc = models.TextField()
    # category = models.ForeignKey(Category)

    class Meta:
        verbose_name_plural = 'Profil'
        verbose_name = 'Profil UMKM'
        app_label = string_with_title("umkm", "Administrasi Pengetahuan")


class Product(models.Model):
    PRODUCT_TYPES = (('P', 'Published'), ('D', 'Draft'))

    name = models.CharField(max_length=200)
    description = models.TextField()
    excerpt = models.TextField()
    status = models.CharField(max_length=1, choices=PRODUCT_TYPES)
    owner = models.ForeignKey(Profile)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name_plural = 'Produk'
        verbose_name = 'Produk'
        app_label = string_with_title("umkm", "Administrasi Pengetahuan")