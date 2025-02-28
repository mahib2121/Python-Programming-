from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="hello"),
    path("Mb", views.Mb, name="MB"),
    path("htmlview/", views.mahib, name="htmlview"),
]
