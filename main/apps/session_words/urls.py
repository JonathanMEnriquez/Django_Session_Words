from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^sessionwords$', views.session),
    url(r'^reset$', views.reset),
    url(r'^process$', views.process),
]