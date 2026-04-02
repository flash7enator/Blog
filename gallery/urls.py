from django.urls import path
from . import views


app_name = 'gallery'

urlpatterns = [
    path('', views.gallery_list, name='gallery'),
    path('upload/', views.upload, name='gallery_upload'),
]