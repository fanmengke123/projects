from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^upload/$', views.upload),
    url(r'^page_text/(\d*)$', views.page_text),
    url(r'^index3/$', views.index3),
    url(r'^pro/$', views.pro),
    url(r'^city/(\d+)/$', views.city)
]
