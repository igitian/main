# the URLconf file for race app

from django.conf.urls import patterns, url

from race import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^user/(?P<user_id>\d+)/$', views.user, name='user'),
    url(r'^action/$', views.action, name='action'),
    url(r'^top/users$', views.topusers, name='topusers'),
)

