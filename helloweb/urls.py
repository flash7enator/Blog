from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="home"),
    path('page/', views.page, name="page"),
    path('blog/', views.blog, name="blog"),
    path('archive/', views.archive, name="archive"),

    path('datetime/', views.current_datetime, name="datetime"),
    path('datetime_class/', views.CurrentDateTime.as_view())
]
