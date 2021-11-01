from django.urls import path
from .views import  about, blog


app_name = 'blog'

urlpatterns = [
    path('' , blog , name='blg'),
    path('about/', about, name= 'about')
]