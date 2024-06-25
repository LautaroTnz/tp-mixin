## Uso del Mixin SuperUserRequiredMixin

El mixin `SuperUserRequiredMixin` se utiliza para gestionar la autenticación y redirección de usuarios basándose en si son superusuarios o no. A continuación, se explica cómo integrarlo en las vistas del proyecto:

### Código del Mixin

El código del mixin se encuentra en `myapp/mixins.py`:

```python
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
```
Explicación del Funcionamiento
-
#### test_func(self):
Este método verifica si el usuario actual (self.request.user) es un superusuario (is_superuser). Devuelve True si lo es y False en caso contrario.

#### handle_no_permission(self):
Método llamado cuando test_func devuelve False, redirige al usuario a la vista 'usuario' destinada a los usuarios normales.

#### form_valid(self, form):
Método que se ejecuta cuando el formulario de inicio de sesión es válido.
Inicia sesión con el usuario autenticado usando login(self.request, form.get_user()).
Redirige al usuario a diferentes vistas según su tipo:
Si es superusuario, redirige a la vista 'superusuario'.
Si no es superusuario, redirige a la vista 'usuario'.
Este mixin se utiliza en las vistas del proyecto para asegurar que las redirecciones se manejen correctamente basándose en el tipo de usuario que inicia sesión.


### Usuarios de prueba

- usuario: admin contraseña: contraseña1234

- usuario: usuarioprueba1 contraseña: contraseña1234

-

## REALIZADO POR: EMANUEL PADILLA
