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
    list_display = ['title', 'status', 'category', 'num_of_comments']
    exclude = ['post_type']
    form = KnowledgeForm
    fieldsets = [
        ('Post Content',
         {
             'classes': 'full-width',
             'fields': ('title', 'content', 'excerpt', 'category')
         })
    ]


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


def save_model(request, obj, form, change):
    # custom stuff here
    obj.save()


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1
    exclude = ['type', 'owner', 'question', 'answer']

    def save_model(self, request, obj, form, change):
        # custom stuff here
        obj.type = 'A'
        obj.owner = request.user
        obj.save()


class ArticleReadOnly(admin.ModelAdmin):
    list_display = ['title', 'status', 'category', 'num_of_comments']
    exclude = ['post_type', 'files']
    readonly_fields = ['title', 'content', 'excerpt', 'category', 'tags', 'status', 'creator']
    inlines = [CommentInline]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(ArticleRO, ArticleReadOnly)