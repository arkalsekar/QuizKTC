from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("quiz/<int:quiz_id>", views.open_quiz, name="open_quiz"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
]
