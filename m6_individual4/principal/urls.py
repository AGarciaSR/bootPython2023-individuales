from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("users", views.users, name="users"),
    path("user_detail/<int:id_number>", views.user_detail, name="user_detail"),
    path("user_form", views.user_form, name="user_form"),
    path("about", views.about, name="about")
]