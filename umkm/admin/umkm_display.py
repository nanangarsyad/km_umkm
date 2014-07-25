from django.contrib import admin
from umkm.models import *
from django.forms import ModelForm
from suit_redactor.widgets import RedactorWidget


class Response(ModelForm):
    class Meta:
        widgets = {
            'content': RedactorWidget(editor_options={
                'buttons': ['html', '|', 'bold', 'italic']})
        }


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1
    exclude = ['type', 'owner', 'question', 'answer']
    form = Response


class ArticleReadOnly(admin.ModelAdmin):
    list_display = ['title', 'excerpt',  'category', 'status', 'num_of_comments', 'creator']
    readonly_fields = ['title', 'content', 'excerpt', 'category', 'tags', 'status', 'creator']
    inlines = [CommentInline]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.type = 'A'
            instance.owner = request.user
            instance.save()
        formset.save_m2m()


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1
    exclude = ['status', 'owner', 'votes']
    form = Response

    def has_delete_permission(self, request, obj=None):
        return False


class QuestionReadOnly(admin.ModelAdmin):
    list_display = ['title', 'excerpt', 'creator', 'num_answer', 'category', 'status']
    readonly_fields = ['title', 'content', 'excerpt', 'category', 'tags', 'status', 'creator']
    inlines = [AnswerInline]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.votes = 0
            instance.owner = request.user
            instance.save()
        formset.save_m2m()


class TrainingReadOnly(admin.ModelAdmin):
    list_display = ['topic', 'start_date', 'end_date', 'venue', 'organizer', 'training_type']
    readonly_fields = ['topic', 'description', 'start_date', 'end_date', 'venue', 'organizer', 'training_type']

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(ArticleRO, ArticleReadOnly)
admin.site.register(QuestionRO, QuestionReadOnly)
admin.site.register(TrainingRO, TrainingReadOnly)
