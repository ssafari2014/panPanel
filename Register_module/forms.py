from django import forms
from django.core.exceptions import ValidationError


# from django.core import validators


# User input form
class registerForm(forms.Form):
    email = forms.EmailField(label='email',
                             widget=forms.EmailInput(attrs={
                                 'type': 'email'}), )
    password = forms.CharField(label='password',
                               widget=forms.PasswordInput(attrs={
                                   'type': 'password',
                                   'id': 'password',
                                   'name': 'password'
                               }), )
    repeat_password = forms.CharField(label='repeat_password',
                                      widget=forms.PasswordInput(attrs={
                                          'type': 'password',
                                          'id': 'password',
                                          'name': 'password'
                                      }), )

    def clean_repeat_password(self):
        password = self.cleaned_data.get('password')
        repeat_pass = self.cleaned_data.get('repeat_password')
        if password == repeat_pass:
            return repeat_pass
        else:
            raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارد ')


# login Form

class loginForm(forms.Form):
    email = forms.EmailField(label='email',
                             widget=forms.EmailInput(attrs={
                                 'type': 'email'}), )
    password = forms.CharField(label='password',
                               widget=forms.PasswordInput(attrs={
                                   'type': 'password',
                                   'id': 'password',
                                   'name': 'password'
                               }))


class Forget_Password_Form(forms.Form):
    email = forms.EmailField(label='email',
                             widget=forms.EmailInput(attrs={
                                 'type': 'email'}), )


class Reset_Password_Form(forms.Form):
    password = forms.CharField(label='password',
                               widget=forms.PasswordInput(attrs={
                                   'type': 'password',
                                   'id': 'password',
                                   'name': 'password'
                               }), )
    repeat_password = forms.CharField(label='repeat_password',
                                      widget=forms.PasswordInput(attrs={
                                          'type': 'password',
                                          'id': 'password',
                                          'name': 'password'
                                      }), )