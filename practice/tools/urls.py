from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_func, name = "index_func"),
    path("dummy/", views.dummy_home),
    path("dummy/run", views.dummy_home_ex)
]