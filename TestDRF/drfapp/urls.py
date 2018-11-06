from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'publisher_list/$', views.publisher_list),
    url(r'publisher/(\d+)/$', views.publisher_detail)
]
