# myapp/mixins.py

from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin

class SuperUserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('usuario')

    def form_valid(self, form):
        login(self.request, form.get_user())
        # Redirecciona basándose en el tipo de usuario
        if self.request.user.is_superuser:
            return redirect('superusuario')
        else:
            return redirect('usuario')
