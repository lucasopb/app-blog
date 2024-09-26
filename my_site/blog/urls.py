from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page),
    path("posts", views.posts),
    path("detalhes", views.post_datails)
]