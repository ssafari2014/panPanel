from django.shortcuts import render
from django.views import View
from .models import AboutModel
from site_module.models import site_setting

# Create your views here.


class aboutView(View):
    def get(self, request):
        about = AboutModel.objects.all()
        setting: site_setting = site_setting.objects.filter(is_main_setting=True).first()
        return render(request, 'about_module/about.html', context={
            'about': about,
            'setting': setting,
        })
