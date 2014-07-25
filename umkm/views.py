from rest_framework import viewsets
from umkm.serializers import *
from umkm.models.knowledge import *
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string


def login(req):
    title = 'Login Aplikasi Lab Inovasi UMKM';
    return render(req, 'sign-in.html', {'title': title})

def dashboard(req):    
    title = 'Dashboar Aplikasi KM-UMKM'
    return render(req, 'dashboard.html', {'title': title})


def question_adm(req):
    html = '<html><body><h1>List of Question</h1></body></html>'
    return HttpResponse(html)


def question_edit(req, quest_id):
    html = '<html><body><h1>Question number '+quest_id+'</h1></body></html>'
    return HttpResponse(html)


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