import re

from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from main_page.models import Articles
from . import views

urlpatterns = [
    url(r'^$', ListView.as_view(queryset = Articles.objects.all().order_by("time_of_day").order_by("day_of_week"), template_name = "main_page/index.html")),
]