from umkm.models.media import *
from django.contrib.auth.models import User
from umkm.utility import *
from django.utils.html import *

class ArticleManager(models.Manager):

    def get_queryset(self):
        return super(ArticleManager, self).get_queryset  # .filter(post_type=1)


class Article(models.Model):

    POST_STATUS = (
        ('1', 'Published'),
        ('2', 'Draft'),
        ('3', 'Unpublished'),
        ('4', 'Pending'),
        ('5', 'Deleted'),
    )

    title = models.CharField('Judul Artikel', max_length=200)
    content = models.TextField('Konten Artikel')
    excerpt = models.TextField('Ringkasan/Abstrak')
    status = models.CharField(max_length=1, choices=POST_STATUS)
    category = models.ForeignKey(Category, verbose_name='Kategori')
    creator = models.ForeignKey(User, verbose_name= 'Penulis')
    tags = models.ManyToManyField(Tag)
    files = models.ManyToManyField(Media, null=True, blank=True, default=None)

    class Meta:
        verbose_name_plural = 'Artikel'
        verbose_name = 'Artikel'
        app_label = string_with_title("umkm", "Administrasi Pengetahuan")

    def num_of_article(self):
        return self.objects.all().count()

    def num_of_comments(self):
        return Comment.objects.filter(article=self).count()

    def __unicode__(self):
        return self.title


class Question(models.Model):
    POST_STATUS = (
        ('T', 'Terjawab'),
        ('B', 'Belum Terjawab'),
        ('C', 'Batal Bertanya'),
    )

    title = models.CharField('Judul Pertanyaan', max_length=200)
    content = models.TextField('Pertanyaan')
    excerpt = models.TextField('Ringkasan')
    status = models.CharField(max_length=1, choices=POST_STATUS)
    category = models.ForeignKey(Category, verbose_name='Kategori')
    tags = models.ManyToManyField(Tag)
    files = models.ManyToManyField(Media, null=True, blank=True, default=None)
    creator = models.ForeignKey(User, verbose_name='Penanya')

    class Meta:
        verbose_name_plural = 'Pertanyaan'
        verbose_name = 'Pertanyaan'
        app_label = string_with_title("umkm", "Administrasi Pengetahuan")

    def num_answer(self):
        return Answer.objects.filter(question=self).count()

    def __unicode__(self):
        return self.title


class Answer(models.Model):

    ANSWER_STATUS = (
        ('T', 'Tepat'),
        ('M', 'Mendekati'),
        ('O', 'Di luar topik'),
        ('S', 'SPAM'),
        ('N', 'Netral')
    )

    content = models.TextField('Jawaban')
    votes = models.IntegerField('vote', max_length=3)
    status = models.CharField(max_length=1, choices=ANSWER_STATUS)
    question = models.ForeignKey(Question, verbose_name='Pertanyaan')
    owner = models.ForeignKey(User, verbose_name='Penjawab')

    class Meta:
        verbose_name_plural = 'Jawaban'
        verbose_name = 'Jawaban'
        app_label = string_with_title("umkm", "Administrasi Pengetahuan")

    def content_excerpt(self):
        return strip_tags(self.content)[0:70]+"..."

    def __unicode__(self):
        return self.content_excerpt()


class Comment(models.Model):
    COMMENT_TYPES = (
        ('A', 'Artikel'),
        ('Q', 'Pertanyaan'),
        ('S', 'Jawaban'),
        ('P', 'Produk')
    )

    content = models.TextField('Komentar')
    type = models.CharField('Komentar untuk', max_length=1, choices=COMMENT_TYPES)
    owner = models.ForeignKey(User, verbose_name='Penulis')
    article = models.ForeignKey(Article, verbose_name='untuk artikel', null=True, blank=True, default=None)
    question = models.ForeignKey(Question, verbose_name='untuk pertanyaan', null=True, blank=True, default=None)
    answer = models.ForeignKey(Answer, verbose_name='untuk jawaban', null=True, blank=True, default=None)

    class Meta:
        verbose_name_plural = 'Komentar'
        verbose_name = 'Komentar'
        app_label = string_with_title("umkm", "Administrasi Pengetahuan")

    def __unicode__(self):
        return self.content