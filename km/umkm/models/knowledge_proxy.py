from umkm.models.knowledge import *


class ArticleRO(Article):

    class Meta:
        proxy = True
        verbose_name_plural = 'Artikel'
        verbose_name = 'Artikel'
        app_label = 'display_umkm'


class QuestionRO(Question):

    class Meta:
        proxy = True
        verbose_name_plural = 'Pertanyaan'
        verbose_name = 'Pertanyaan'
        app_label = 'display_umkm'


class AnswerRO(Answer):

    class Meta:
        proxy = True
        verbose_name_plural = 'Jawaban'
        verbose_name = 'Jawaban'
        app_label = 'display_umkm'


class CommentRO(Comment):

    class Meta:
        proxy = True
        verbose_name_plural = 'List Komentar'
        verbose_name = 'Komentar'
        app_label = 'display_umkm'