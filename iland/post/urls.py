from django.conf.urls import url, include
from django.contrib import admin

from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    post_list_department
    )

urlpatterns = [
    url(r'^$', post_list, name="list"),
    url(r'^(?P<id>\d+)/$',post_detail, name="detail"),
    url(r'^(?P<id>\d+)/edit/$',post_update, name="edit"),
    url(r'^create/$',post_create),
    url(r'^(?P<id>\d+)/delete/$',post_delete),
    url(r'^(?P<department_name>[\w-]+)/$', post_list_department, name='department'),
]
