from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ServicesPageView(TemplateView):
    template_name = 'services.html'

class ContactusPageView(TemplateView):
    template_name = 'contactus.html'


