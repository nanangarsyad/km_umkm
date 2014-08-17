from rest_framework import viewsets
from umkm.serializers import *
from umkm.models.knowledge import *
from umkm.models.knowledge import Answer
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string


def login(req):
    title = 'Login Aplikasi Lab Inovasi UMKM';
    return render(req, 'sign-in.html', {'title': title})


def dashboard(req):
    title = 'Dashboard Aplikasi KM-UMKM'
    tags = []
    for x in Category.objects.all() :
        if not x.parent :
            data_tag = {'main' : x}
            data_tag['sub'] = []
            for c in Category.objects.all() :
                if c.parent and c.parent.title == x.title :
                    data_tag['sub'].append(c)
            tags.append(data_tag)

    return render(req, 'dashboard.html',
                  {'title': title, 'tags' : tags})


def article_adm(req):
    title = ''
    tags = Category.objects.all()
    return render(req, 'article-list.html', {'title': title,
                                             'tags' : tags})


def article_show(req, quest_id):
    title = ''
    tags = Category.objects.all()
    return render(req, 'article-show.html', {'title': title,
                                             'tags' : tags})


def question_adm(req):
    title = ''
    question_list = Question.objects.all()
    question_tags = Tag.objects.all()
    return render(req, 'question-list.html',
                  {'title': title, 'question_list' : question_list,
                   'question_tags' : question_tags,})


def question_edit(req, quest_id):
    html = '<html><body><h1>Question number '+quest_id+'</h1></body></html>'
    return HttpResponse(html)


def question_show(req, quest_id):
    title = ''
    question = Question.objects.get(id=quest_id)
    answers =  []
    quest_id = int(quest_id)
    for ans in  Answer.objects.all() :
        if ans.question.id == quest_id :
            answers.append(ans)

    return render(req, 'question-show.html',
                  {'title': title,'question' : question,
                   'answers': answers})

def media_adm(req) :
    title = ''
    tags = Category.objects.all()
    return render(req, 'media-list.html', {'title': title,
                                             'tags' : tags})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer