from django import forms
from django.contrib.auth.models import User

class registration_form(forms.Form):
    password = forms.CharField(label='Password', max_length=25)
    confirm_password = forms.CharField(label='Confirm Password', max_length=25)
    username = forms.CharField(label='Username', max_length=25)
    referal_code = forms.CharField(max_length=12)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

    def clean_password(self):
        password = self.cleaned_data.get("password")
        special_characters = ["^", "%", "$", "#", "@", "!", "&", "*"]
        has_special_character = any(char in password for char in special_characters)

        if not has_special_character:
            raise forms.ValidationError("Password must contain at least one special character")

        if password.islower():
            raise forms.ValidationError("Password must contain an uppercase letter")

        return password

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("User with this username already exists")
        return username
