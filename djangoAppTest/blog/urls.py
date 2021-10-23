from django.urls import path
from .views import index, about

app_name = 'blog'

urlpatterns = [
    path('home/', index, name='index'),
]