from django.contrib.auth import forms
from django.contrib.auth.models import User
class UserRegisterForm(forms.UserCreationForm):
    

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "passwprd1", "password2"]
        help_texts = {k:"" for k in fields}
        