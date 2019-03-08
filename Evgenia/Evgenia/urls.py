from django.contrib import admin
from django.urls import path, include
import re

urlpatterns = [
    path('admin/', admin.site.urls),
    path('groups/', include('main_page.urls')), 
]
