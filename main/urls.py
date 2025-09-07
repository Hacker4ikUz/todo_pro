from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("done/<int:task_id>/", views.task_done, name="task_done"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
