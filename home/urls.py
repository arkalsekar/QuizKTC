from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("quiz/<int:quiz_id>", views.open_quiz, name="open_quiz"),
    path("submit", views.submit, name="submit"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("signup", views.signup, name='signup'),
    path("login", views.handle_login, name='handle_login'),
    path("logout", views.handle_logout, name='logout'), 

]
