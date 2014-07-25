from django.contrib import admin
from umkm.models import *
from django.forms import ModelForm
from suit_redactor.widgets import RedactorWidget


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'parent']


class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class KnowledgeForm(ModelForm):
    class Meta:
        widgets = {
            'content': RedactorWidget(editor_options={'lang': 'en'}),
            'excerpt': RedactorWidget(editor_options={
                'buttons': ['html', '|', 'bold', 'italic']})
        }


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'excerpt',  'category', 'status', 'num_of_comments', 'creator']
    form = KnowledgeForm
    fieldsets = [
        ('Post Content',
         {
             'classes': 'full-width',
             'fields': ('title', 'content', 'excerpt', 'category', 'tags', 'status')
         })
    ]

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        obj.save()


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'type', 'article', 'question', 'answer', 'owner']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'excerpt', 'creator', 'num_answer', 'category', 'status']
    form = KnowledgeForm


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['content', 'votes', 'question', 'owner', 'status']


class MediaAdmin(admin.ModelAdmin):
    list_display = ['title', 'creator', 'media_file', 'shareable']


class TrainingAdmin(admin.ModelAdmin):
    list_display = ['topic', 'start_date', 'end_date', 'venue', 'organizer', 'training_type']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Comment, CommentAdmin)