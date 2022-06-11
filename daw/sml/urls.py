from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
import re
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from .views import *

urlpatterns = [
    path('sml_vew/', sml_vew, name= "sml_view"),
    path('creacion/', creacion, name="creacion"),
    path('lectura/', lectura, name="lectura"),
  
]