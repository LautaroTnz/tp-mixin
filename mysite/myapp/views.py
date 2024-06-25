from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import SuperUserRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy

class SuperUsuarioView(LoginRequiredMixin, SuperUserRequiredMixin, TemplateView):
    template_name = 'myapp/superusuario.html'

class UsuarioView(LoginRequiredMixin, TemplateView):
    template_name = 'myapp/usuario.html'

class CustomLoginView(LoginView, SuperUserRequiredMixin):
    template_name = 'myapp/login.html'
    form_class = AuthenticationForm
