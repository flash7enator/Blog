from . import views
from django.urls import path

app_name = 'order'

urlpatterns = [
    path('', views.order_create, name='order_create'),
]