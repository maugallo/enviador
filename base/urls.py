from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("enviar-email/", views.emailView, name="enviar"),
    path("success/", views.emailSuccess, name="success"),
    path("failed/", views.emailFailed, name="failed"),
]
