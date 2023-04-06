from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import FormView

from .forms import RegisterForm, ContactUsForm


class RegisterLoginView(View):
    def get(self, request):
        register_form = RegisterForm()
        login_form = AuthenticationForm()
        return render(request, 'events/index.html', {'register_form': register_form, 'login_form': login_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        login_form = AuthenticationForm(request, data=request.POST)

        if register_form.is_valid():
            user = register_form.save()
            email = register_form.cleaned_data.get('email')
            raw_password = register_form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('index')

        elif login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')

        return render(request, 'events/index.html', {'register_form': register_form, 'login_form': login_form})


class ContactUsView(FormView):
    template_name = "events/contact_us.html"
    form_class = ContactUsForm
