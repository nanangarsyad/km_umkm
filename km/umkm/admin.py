from django.contrib import admin
from umkm.models import *

# Register your models here.


class TypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'type_for', 'creator']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'parent']


class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_title', 'description']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'status', 'post_category', 'num_comment']
    exclude = ['post_type']


class AnswerInline(admin.TabularInline):
    model = Answer.relationsip.through
    extra = 1
    fk_name = 'to_knowledge'
    exclude = ['relation_type']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'status', 'post_category', 'num_answer']
    inlines = [AnswerInline]


class MediaAdmin(admin.ModelAdmin):
    list_display = ['title', 'creator', 'media_type', 'shareable']


class TrainingAdmin(admin.ModelAdmin):
    list_display = ['topic', 'start_date', 'end_date', 'venue', 'organizer', 'training_type']


admin.site.register(Type, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Relationship)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Media, MediaAdmin)