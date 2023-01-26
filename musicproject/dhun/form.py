from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class Register(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,max_length=10)
    re_password=forms.CharField(widget=forms.PasswordInput,max_length=10)
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
    def clean(self):
        super().clean()  #we are accesing the predifend clean in model form for the fields like username,etc
        p=self.cleaned_data.get('password')
        p1=self.cleaned_data.get('re_password')
        if p!=p1:
            raise forms.ValidationError('password did not match')

class Login(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput,max_length=10)
    def clean(self):
        u=self.cleaned_data.get("username")
        p=self.cleaned_data.get("password")
        val=authenticate(username=u,password=p)
        if val is None:
            raise forms.ValidationError("user/password didnot match")

