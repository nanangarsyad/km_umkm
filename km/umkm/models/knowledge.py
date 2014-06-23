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
    # type = models.ForeignKey(Type)
    category = models.ForeignKey(Category)
    creator = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)
    files = models.ManyToManyField(Media, null=True, blank=True, default=None)
    # relationsip = models.ManyToManyField('self', through='Relationship',
    #                                      symmetrical=False, related_name='related_to')

    class Meta:
        verbose_name_plural = 'Artikel'
        verbose_name = 'Artikel'
        app_label = 'umkm'

    def numOfArticle(self):
        return self.objects.all().count()

    def numOfComments(self):
        return Comment.objects.filter(article=self).count()


    # objects = ArticleManager()

    # def save(self, *args, **kwargs):
    #     self.post_type = Type.objects.get(title__exact='Artikel')
    #     super(Article, self).save(*args, **kwargs)

        # return len(list(Knowledge.objects.raw("""select * from umkm_knowledge k
        #                 join umkm_relationship r on (k.id = r.to_knowledge_id)
        #                 where r.relation_type_id = 7 and k.id = %s""", [self.id])))


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
        verbose_name_plural = 'Pertanyaan'
        verbose_name = 'Pertanyaan'
        app_label = 'umkm'

    def num_answer(self):
        return self.objects.count()

            # len(list(Knowledge.objects.raw("""select * from umkm_knowledge k
            #             join umkm_relationship r on (k.id = r.to_knowledge_id)
            #             where r.relation_type_id = 6 and k.id = %s""", [self.id])))


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
        verbose_name_plural = 'Jawaban'
        verbose_name = 'Jawaban'
        app_label = 'umkm'


# class Relationship(models.Model):
#     from_knowledge = models.ForeignKey(Knowledge, related_name='from')
#     to_knowledge = models.ForeignKey(Knowledge, related_name='to')
#     relation_type = models.ForeignKey(Type)
#
#     class Meta:
#         app_label = 'umkm'

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