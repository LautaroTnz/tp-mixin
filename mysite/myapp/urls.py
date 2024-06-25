from django.urls import path
from .views import SuperUsuarioView, UsuarioView,CustomLoginView

urlpatterns = [
    path('superusuario/', SuperUsuarioView.as_view(), name='superusuario'),
    path('usuario/', UsuarioView.as_view(), name='usuario'),
    path('', CustomLoginView.as_view(), name='login'),
]
