from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index/index.html'


class ContactUs(TemplateView):
    template_name = 'index/contact.html'
