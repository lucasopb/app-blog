from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_datails,
         name="post-datails-page")
]