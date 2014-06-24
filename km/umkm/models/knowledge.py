from umkm.models.media import *
from django.contrib.auth.models import User


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

    title = models.CharField(max_length=200)
    content = models.TextField()
    excerpt = models.TextField()
    status = models.CharField(max_length=1, choices=POST_STATUS)
    category = models.ForeignKey(Category)
    creator = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)
    files = models.ManyToManyField(Media, null=True, blank=True, default=None)

    class Meta:
        verbose_name_plural = 'Manajer Artikel'
        verbose_name = 'Artikel'
        app_label = 'umkm'

    def num_of_article(self):
        return self.objects.all().count()

    def num_of_comments(self):
        return Comment.objects.filter(article=self).count()


class Question(models.Model):
    POST_STATUS = (
        ('T', 'Terjawab'),
        ('B', 'Belum Terjawab'),
        ('C', 'Batal Bertanya'),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    excerpt = models.TextField()
    status = models.CharField(max_length=1, choices=POST_STATUS)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    files = models.ManyToManyField(Media, null=True, blank=True, default=None)
    creator = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = 'Manajer Pertanyaan'
        verbose_name = 'Pertanyaan'
        app_label = 'umkm'

    def num_answer(self):
        return self.objects.count()


class Answer(models.Model):

    ANSWER_STATUS = (
        ('T', 'Tepat'),
        ('M', 'Mendekati'),
        ('O', 'Di luar topik'),
        ('S', 'SPAM')
    )

    content = models.TextField()
    votes = models.IntegerField(max_length=3)
    status = models.CharField(max_length=1, choices=ANSWER_STATUS)
    question = models.ForeignKey(Question)
    owner = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = 'Manajer Jawaban'
        verbose_name = 'Jawaban'
        app_label = 'umkm'


class Comment(models.Model):
    COMMENT_TYPES = (
        ('A', 'Artikel'),
        ('Q', 'Pertanyaan'),
        ('S', 'Jawaban')
    )

    comment = models.TextField()
    type = models.CharField(max_length=1, choices=COMMENT_TYPES)
    owner = models.ForeignKey(User)
    article = models.ForeignKey(Article)
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answer)

    class Meta:
        verbose_name_plural = 'List Komentar'
        verbose_name = 'Komentar'
        app_label = 'umkm'