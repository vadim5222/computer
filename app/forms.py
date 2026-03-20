from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from app.models import User


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'login')


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')