from django.contrib import admin
from umkm.models import *
from django.forms import ModelForm
from suit_redactor.widgets import RedactorWidget


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'parent']


class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_title', 'description']


class KnowledgeForm(ModelForm):
    class Meta:
        widgets = {
            'content': RedactorWidget(editor_options={'lang': 'en'}),
            'excerpt': RedactorWidget(editor_options={
                'buttons': ['html', '|', 'bold', 'italic']})
        }


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'category', 'numOfComments']
    exclude = ['post_type']
    form = KnowledgeForm
    fieldsets = [
        ('Post Content',
         {
             'classes': 'full-width',
             'fields': ('title', 'content', 'excerpt', 'category')
         })
    ]

    # def save_model(self, request, obj, form, change):
    #     obj.creator = request.user
    #     obj.save()


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'category', 'num_answer']
    inlines = [AnswerInline]
    form = KnowledgeForm


class MediaAdmin(admin.ModelAdmin):
    list_display = ['title', 'creator', 'shareable']


class TrainingAdmin(admin.ModelAdmin):
    list_display = ['topic', 'start_date', 'end_date', 'venue', 'organizer', 'training_type']


# admin.site.register(Type, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Relationship)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Media, MediaAdmin)