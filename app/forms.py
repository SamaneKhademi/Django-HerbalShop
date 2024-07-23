from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordResetForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import Customer


class LoginForm(AuthenticationForm):
    username = UsernameField(label='نام کاربری' ,widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(attrs={'class':'form-control'}))


class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(label='نام کاربری', widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    email = forms.CharField(label='ایمیل', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='رمز عبور قبلی', widget=forms.PasswordInput(attrs={'autofocus': True, 'class': 'form-control'}))
    new_password1 = forms.CharField(label='رمز عبور جدید', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='تکرار رمز عبور جدید', widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(attrs={'class': 'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='رمز عبور جدید', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='تکرار رمز عبور جدید', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'mobile', 'state', 'city', 'locality', 'zipcode')
        labels = {'name': 'نام', 'mobile': 'موبایل', 'state': 'استان', 'city': 'شهرستان', 'locality': 'آدرس', 'zipcode': 'کدپستی'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'})
        }

