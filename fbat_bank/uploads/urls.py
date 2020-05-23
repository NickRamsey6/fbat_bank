"""Defines URL patterns for uploads."""

from django.urls import url, path
from uploads.views import statement_upload

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    path('upload-csv/', statement_upload, name="statement_upload"),
]

