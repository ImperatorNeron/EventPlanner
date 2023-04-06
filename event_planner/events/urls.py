from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

from .views import ContactUsView

urlpatterns = [
    path("", views.RegisterLoginView.as_view(), name="index"),
    path("logout/", LogoutView.as_view(next_page="index"), name="logout"),
    path("contact-us/", ContactUsView.as_view(), name="contact_us"),
]
