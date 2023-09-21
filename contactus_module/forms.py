from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import ContactusModel
from django import forms


class ContactusForm(ModelForm):
    class Meta:
        model = ContactusModel
        fields = ['first_name', 'last_name', 'subject', 'message']

        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی ',
            'subject': 'عنوان',
            'message': 'متن پیام'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'type': 'text',
                'size': 40,
                'class': 'wpcf7-form-control wpcf7-text wpcf7-validates-as-required input-text',
                'aria-invalid': 'false',
                'value name': 'first-name'
            }),
            'last_name': forms.TextInput(attrs={
                'type': 'text',
                'size': 40,
                'class': 'wpcf7-form-control wpcf7-text wpcf7-validates-as-required input-text',

            }),
            'subject': forms.TextInput(attrs={
                'type': 'text',
                'size': 40,
                'class': 'wpcf7-form-control wpcf7-text wpcf7-validates-as-required input-text',

            }),
            'message': forms.Textarea(attrs={
                'class': 'wpcf7-form-control wpcf7-textarea',
                'rows': '10',
                'cols': '40',
            }),
        }

        error_messages = {
            'first_name': {
                'required': 'وارد کردن نام الزامی است'
            },
            'last_name': {
                'required': 'وارد کردن نام خانوادگی الزامی است'
            },
            'subject': {
                'required': 'وارد کردن عنوان پیام الزامی است'
            },
            'message': {
                'required': 'وارد کردن متن پیام الزامی است'
            },

        }

    # def clean_first_name(self):
    #     first_Name = self.cleaned_data.get('first_name')
    #     last_Name = self.cleaned_data.get('last_name')
    #     if first_Name == last_Name:
    #         raise ValidationError('نام و نام خانوادگی نمی تواند یکسان باشد')
    #     else:
    #         return last_Name


