from django.db import models
from umkm.models.profile import Profile

class Category(models.Model):
	CAT_FOR = (('K', 'Knowledge'), ('P', 'Profile'))

	name = models.CharField(max_length=200)	
	description = models.TextField()
	parent = models.ForeignKey('self', null=True, blank=True, default = None)
	category_for = models.CharField(max_length = 1, choices = CAT_FOR)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'List Kategori'
		verbose_name = 'Kategori'
		app_label = 'umkm'

class Type(models.Model):
	FOR_TYPE = (('K', 'Knowledge'), ('R', 'Relation'), ('M', 'Media'), ('P', 'Profile'))

	title = models.CharField(max_length=200)
	type_for = models.CharField(max_length = 1, choices = FOR_TYPE )
	creator = models.ForeignKey(Profile)

	def __unicode__(self):
		return self.title

	class Meta:		
		verbose_name_plural = 'List Tipe'
		verbose_name = 'Tipe'
		app_label = 'umkm'

class Tag(models.Model):
	TAG_FOR = (('K', 'Knowledge'), ('P', 'Profile'))

	tag_title = models.CharField(max_length=200)
	description = models.TextField()
	tag_for = models.CharField(max_length = 1, choices = TAG_FOR)

	def __unicode__(self):
		return self.tag_title

	class Meta:		
		verbose_name_plural = 'List Label'
		verbose_name = 'Label'
		app_label = 'umkm'