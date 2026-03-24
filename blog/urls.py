from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name="home"),
    path('contacts/', views.contacts, name="contacts"),
    path('post/<slug:slug>', views.post_detail, name="post_detail"),
    path('category/<slug:slug>', views.category, name="category"),
    path('tag/<slug:slug>', views.posts_by_tag, name="tag"),
    path('search/', views.search, name="search"),
    path('create-post/', views.create_post, name='create_post'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/<slug:slug>/delete/', views.post_delete, name='post_delete'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('subscribe/', views.subscribe, name="subscribe"),
    path('profile/', views.profile, name='profile'),

]
