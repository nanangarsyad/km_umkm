
from django.conf.urls import patterns, include, url
from rest_framework import routers
from django.contrib import admin

from umkm import views
from km import settings

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'articles', views.ArticleViewSet)

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'km.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^admin/',  include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

urlpatterns += patterns('umkm.views',
        url(r'^backend/$', 'dashboard'),
        url(r'^backend/quests/$', 'question_adm'),
        url(r'^backend/quest/(?P<quest_id>\d+)/', 'question_edit'),
        url(r'^login/$', 'login'),
)