from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^activities/$', views.activities, name='activitites'),
    url(r'^activity/(?P<pk>\d+)/$', views.activity_detail, name='activity_detail')
]