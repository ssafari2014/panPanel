from django.shortcuts import render
from django.views.generic import View
from site_module.models import site_setting, FooterLinkBoxModel


# Create your views here.

# This view is related to the index page of the site
class indexView(View):
    def get(self, request):
        return render(request, 'home_module/home.html')


class header_partial(View):
    def get(self, request):
        setting: site_setting = site_setting.objects.filter(is_main_setting=True).first()
        return render(request, 'base/header_partial.html', context={
            'setting': setting
        })


class footer_partial(View):
    def get(self, request):
        setting: site_setting = site_setting.objects.filter(is_main_setting=True).first()
        footer_link_boxs = FooterLinkBoxModel.objects.all()
        return render(request, 'base/footer_partial.html', context={
            'setting': setting,
            'footer_link_boxs': footer_link_boxs
        })


class header_site(View):
    def get(self, request):
        return render(request, 'base/header_site.html')


class footer_site_ref(View):
    def get(self, request):
        return render(request, 'base/footer_site.html')
