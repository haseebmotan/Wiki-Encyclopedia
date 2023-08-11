from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.display_entry, name="display_entry"),
    path("error", views.error, name="error"),
    path("new", views.newpage, name="newpage"),
    path("random_page", views.random_page, name="random_page"),
    path("edit/<str:entry>", views.edit_entry, name="edit_entry")
]
