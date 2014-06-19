from umkm.models.media import *
from django.contrib.auth.models import User


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
    status = models.CharField(max_length=1, choices=POST_STATUS)
    post_type = models.ForeignKey(Type)
    post_category = models.ForeignKey(Category)
    creator = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)
    files = models.ManyToManyField(Media, null=True, blank=True, default=None)
    relationsip = models.ManyToManyField('self', through='Relationship',
                                         symmetrical=False, related_name='related_to')

    class Meta:
        app_label = 'umkm'

    def __unicode__(self):
        return self.post_title


class ArticleManager(models.Manager):

    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(post_type=1)


class Article(Knowledge):

    class Meta:
        proxy = True
        verbose_name_plural = 'Artikel'
        verbose_name = 'Artikel'
        app_label = 'umkm'

    objects = ArticleManager()

    def display_record(self):
        return self.filter(post_type=1)

    def save(self, *args, **kwargs):
        self.post_type = Type.objects.get(title__exact='Artikel')
        super(Article, self).save(*args, **kwargs)

    def num_comment(self):
        return len(list(Knowledge.objects.raw("""select * from umkm_knowledge k 
                        join umkm_relationship r on (k.id = r.to_knowledge_id) 
                        where r.relation_type_id = 7 and k.id = %s""", [self.id])))


class ProductManager(models.Manager):

    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(post_type=5)


class Product(Knowledge):
    class Meta:
        proxy = True
        verbose_name_plural = 'Produk'
        verbose_name = 'Produk'
        app_label = 'umkm'

    def save(self, *args, **kwargs):
        self.post_type = Type.objects.get(title__exact='Produk')
        super(Product, self).save(*args, **kwargs)

    objects = ProductManager()


class QuestManager(models.Manager):

    def get_queryset(self):
        return super(QuestManager, self).get_queryset().filter(post_type=2)


class Question(Knowledge):
    POST_STATUS = (
        ('T', 'Terjawab'),
        ('B', 'Belum Terjawab'),
        ('C', 'Batal Bertanya'),
    ) # userless

    class Meta:
        proxy = True
        verbose_name_plural = 'Pertanyaan'
        verbose_name = 'Pertanyaan'
        app_label = 'umkm'

    def save(self, *args, **kwargs):
        self.post_type = Type.objects.get(title__exact='Pertanyaan')
        super(Product, self).save(*args, **kwargs)

    def num_answer(self):
        return len(list(Knowledge.objects.raw("""select * from umkm_knowledge k 
                        join umkm_relationship r on (k.id = r.to_knowledge_id) 
                        where r.relation_type_id = 6 and k.id = %s""", [self.id]))) 

    objects = QuestManager()


class AnswerManager(models.Manager):

    def get_queryset(self):
        return super(AnswerManager, self).get_queryset().filter(post_type=3)


class Answer(Knowledge):

    class Meta:
        proxy = True
        verbose_name_plural = 'Jawaban'
        verbose_name = 'Jawaban'
        app_label = 'umkm'

    def save(self, *args, **kwargs):
        self.post_type = Type.objects.get(title__exact='Jawaban')
        super(Product, self).save(*args, **kwargs)

    objects = AnswerManager()


class CommentManager(models.Manager):

    def get_queryset(self):
        return super(CommentManager, self).get_queryset().filter(post_type=4)


class Comment(Knowledge):
    class Meta:
        proxy = True
        verbose_name_plural = 'Komentar'
        verbose_name = 'Komentar'
        app_label = 'umkm'

    def save(self, *args, **kwargs):
        self.post_type = Type.objects.get(title__exact='Komentar')
        super(Product, self).save(*args, **kwargs)

    objects = CommentManager()


class Relationship(models.Model):
    from_knowledge = models.ForeignKey(Knowledge, related_name='from')
    to_knowledge = models.ForeignKey(Knowledge, related_name='to')
    relation_type = models.ForeignKey(Type)

    class Meta:
        app_label = 'umkm'
