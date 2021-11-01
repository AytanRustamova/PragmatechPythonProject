from django.urls import path
from .views import  about, blog, blog_detail


app_name = 'blog'

urlpatterns = [
    path('' , blog , name='blg'),
    path('about/', about, name= 'about'),
    path('blog-detail/<slug:slug>/', blog_detail, name='blog-detail')
]