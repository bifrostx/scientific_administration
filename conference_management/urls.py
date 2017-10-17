from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views

app_name = 'conference_management'

urlpatterns = [
    url(r'^$', views.index, name='index'),

]