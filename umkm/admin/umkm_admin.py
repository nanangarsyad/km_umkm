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
             'fields': ('creator', 'title', 'content', 'excerpt', 'category', 'tags', 'status')
         })
    ]

    # def save_model(self, request, obj, form, change):
    #     obj.creator = request.user
    #     obj.save()


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'type', 'article', 'question', 'answer', 'owner']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'excerpt', 'creator', 'num_answer', 'category', 'status']
    form = KnowledgeForm


class AnswerForm(ModelForm):
    class Meta:
        widgets = {
            'content': RedactorWidget(editor_options={'lang': 'en'}),
        }


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'votes', 'question', 'owner', 'status']
    form = AnswerForm


class MediaAdmin(admin.ModelAdmin):
    list_display = ['title', 'creator', 'media_file', 'shareable']


class TrainingAdmin(admin.ModelAdmin):
    list_display = ['topic', 'start_date', 'end_date', 'venue', 'organizer', 'training_type']


class ProfileForm(ModelForm):
    class Meta:
        widgets = {
            'instance_desc': RedactorWidget(editor_options={'lang': 'en'}),
        }


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_type', 'address', 'instance_name']
    form = ProfileForm
    # fieldsets = [
    #     ('Deskripsi Profil',
    #      {
    #          'classes': 'full-width',
    #          'fields': ('user', 'user_type', 'address', 'instance_name', 'instance_desc')
    #      })
    # ]


class ProductForm(ModelForm):
    class Meta:
        widgets = {
            'description': RedactorWidget(editor_options={'lang': 'en'}),
            'excerpt': RedactorWidget(editor_options={
                'buttons': ['html', '|', 'bold', 'italic']})
        }


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'owner', 'category']
    form = ProductForm

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Product, ProductAdmin)