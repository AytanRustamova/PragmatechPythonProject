from django.urls import path, include
from .views import stoires


app_name = 'stories'

urlpatterns = [
    path('', stoires, name="stories")
] 