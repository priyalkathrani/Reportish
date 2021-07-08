from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name='Home-Page'),
    path('submit',views.createPost, name="createPost")
]