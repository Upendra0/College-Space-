from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from . import models 
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField( label= "Password", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField( label = "Confirm Password", widget=forms.PasswordInput, required=True)
  
    class Meta:
        model = models.User
        fields = ['email', 'first_name', 'last_name', 'department', 'semester']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user 

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = models.User
        fields = ['email', 'first_name', 'last_name', 'semester']