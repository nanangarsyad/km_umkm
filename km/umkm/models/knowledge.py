from django.db import models
from umkm.models.species import *
from umkm.models.media import *
from umkm.models.profile import Profile

class Knowledge(models.Model):
	POST_STATUS = (
					('1', 'Published'),
					('2', 'Draft'),
					('3', 'Unpublished'),
					('4', 'Pending'),
					('5', 'Deleted'),
				)

	post_title = models.CharField(max_length=200)
	post_content = models.TextField()
	post_excerpt = models.TextField()
	status = models.BooleanField()
	post_type = models.CharField(max_length = 1, choices = POST_STATUS)
	post_category = models.ForeignKey(Category)
	creator = models.ForeignKey(Profile)
	tags = models.ManyToManyField(Tag)
	files = models.ManyToManyField(Media, null = True, blank = True, default = None)
	relationsip = models.ManyToManyField('self', through = 'Relationship', 
								symmetrical = False, related_name = 'related_to')		

	class Meta:		
		app_label = 'umkm'

	def __unicode__(self):
		return self.post_title

class Article(Knowledge):

	class Meta:
		proxy= True		
		verbose_name_plural = 'List Artikel'
		verbose_name = 'Artikel'
		app_label = 'umkm'

	def save(self, *args, **kwargs):
		self.post_type = Type.objects.get(title__exact = 'Artikel')
		super(Article, self).save(*args, **kwargs)

class Product(Knowledge):
	
	class Meta:
		proxy = True
		verbose_name_plural = 'List Produk'
		verbose_name = 'Produk'
		app_label = 'umkm'

	def save(self, *args, **kwargs):
		self.post_type = Type.objects.get(title__exact = 'Produk')
		super(Product, self).save(*args, **kwargs)

class Relationship(models.Model):
	from_knowledge = models.ForeignKey(Knowledge, related_name = 'from')
	to_knowledge = models.ForeignKey(Knowledge, related_name = 'to')
	relation_type = models.ForeignKey(Type)

	class Meta:		
		app_label = 'umkm'
		