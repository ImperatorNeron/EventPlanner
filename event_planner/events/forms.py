from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User

from events.models import ContactUs


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

        widgets = {
            "username": forms.TextInput(attrs={'class': 'username'}),
            "email": forms.EmailInput(attrs={'class': 'email'}),
            "password1": forms.PasswordInput(attrs={'class': 'password'}),
            "password2": forms.PasswordInput(attrs={'class': 'password'}),
        }


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ("email", "topic", "text",)

        widgets = {
            "email": forms.EmailInput(attrs={"class": "field"}),
            "topic": forms.TextInput(attrs={"class": "field"}),
            "text": forms.Textarea(attrs={"class": "field text-field"}),
        }
