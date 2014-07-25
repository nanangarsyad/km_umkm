from umkm.models.knowledge import *
from umkm.utility import *


class ArticleRO(Article):

    class Meta:
        proxy = True
        verbose_name_plural = 'Artikel'
        verbose_name = 'Artikel'
        app_label = string_with_title("umkm_display", "Manajemen Pengetahuan")


class QuestionRO(Question):

    class Meta:
        proxy = True
        verbose_name_plural = 'Pertanyaan'
        verbose_name = 'Pertanyaan'
        app_label = string_with_title("umkm_display", "Manajemen Pengetahuan")


class AnswerRO(Answer):

    class Meta:
        proxy = True
        verbose_name_plural = 'Jawaban'
        verbose_name = 'Jawaban'
        app_label = string_with_title("umkm_display", "Manajemen Pengetahuan")


class CommentRO(Comment):

    class Meta:
        proxy = True
        verbose_name_plural = 'List Komentar'
        verbose_name = 'Komentar'
        app_label = string_with_title("umkm_display", "Manajemen Pengetahuan")