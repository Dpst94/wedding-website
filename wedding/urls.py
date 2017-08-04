from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^activities/$', views.activity_list, name='activity_list'),
    url(r'^activity/(?P<pk>\d+)/$', views.activity_detail, name='activity_detail'),
    url(r'^activity/new/$', views.activity_new, name='activity_new'),
    url(r'^activity/(?P<pk>\d+)/edit/$', views.activity_edit, name='activity_edit'),
    url(r'^activity/(?P<pk>\d+)/remove/$', views.activity_remove, name='activity_remove'),
    url(r'^rsvp/$', views.rsvp, name='rsvp'),
    url(r'^guestbook/$', views.guestbook, name='guestbook'),
    url(r'^contact/$', views.contact, name='contact'),
]