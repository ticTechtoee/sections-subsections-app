from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from create_sections import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index)
    
]
