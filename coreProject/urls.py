
# Importa el módulo de administración de Django
from django.contrib import admin
# Importa la función 'path' para definir las rutas URL
from django.urls import path
# Importa las vistas 'formularioContacto' y 'contactar' desde el módulo 'academica.views'
from academica.views import Home, Estudiantes, Carreras, Cursos, Matriculas, formularioContacto, contactar

# Define las URL de la aplicación
urlpatterns = [
   # URL para acceder a la interfaz de administración de Django
path('admin/', admin.site.urls),

# URL para mostrar la pagna de inicio
path('', Home),

path('estudiantes/', Estudiantes, name='estudiantes'), 
path('carreras/', Carreras),
path('cursos/', Cursos),
path('matriculas/', Matriculas),

# URL para mostrar el formulario de contacto
path('contacto/', formularioContacto),

# URL para procesar el formulario de contacto (enviar correo)
path('contactar/', contactar)
]






