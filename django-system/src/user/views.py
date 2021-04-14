from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import SignupForm


class SignupView(CreateView):
    template_name = 'user/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('index:index')


class LoginView(TemplateView):
    template_name = 'user/login.html'


class ProfileView(TemplateView):
    template_name = 'user/profile.html'


class LogoutView(TemplateView):
    template_name = 'user/logout.html'
