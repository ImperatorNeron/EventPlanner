from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import RegisterForm, ContactUsForm


class Index(TemplateView):
    template_name = "events/index.html"


class RegistrationView(FormView):
    form_class = RegisterForm
    template_name = "events/registration.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistrationView, self).form_valid(form)


class LogInView(LoginView):
    fields = "__all__"
    template_name = "events/login.html"

    def get_success_url(self):
        return reverse_lazy("index")


class ContactUsView(FormView):
    template_name = "events/contact_us.html"
    form_class = ContactUsForm
