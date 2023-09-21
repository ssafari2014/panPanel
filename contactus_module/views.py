from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ContactusForm


# Create your views here.

class ContactUsView(FormView):
    template_name = 'contactus_module/contactus.html'
    form_class = ContactusForm
    success_url = '/contact_us/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
