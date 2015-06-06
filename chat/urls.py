from django.conf.urls import *
from chat.models import * 
from chat import views

urlpatterns = patterns('',
    url(r'^session/', views.index, name='index'),
    url(r'^register/', views.register, name='register'),
    url(r'^home/', views.user_login, name='home'),
    url(r'^vote/', views.vote,name='vote'),
    #url(r'^test/', views.test,name='test'),
    url(r'^test/', views.test, name='test'),
    url(r'^stats/', views.stats, name='stats'),
)
