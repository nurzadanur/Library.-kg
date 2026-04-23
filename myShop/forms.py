from django import forms
from .models import CustomUser
from captcha.fields import CaptchaField

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = [
            'username', 'password',
            'full_name', 'phone', 'age',
            'city', 'country', 'address',
            'university', 'faculty',
            'avatar', 'passport_file'
        ]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()