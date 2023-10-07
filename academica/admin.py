# Importa el módulo de administración de Django
from django.contrib import admin
# Importa todos los modelos definidos en el módulo 'academica.models'
from academica.models import *

# Registra los modelos en el panel de administración de Django

# Registra el modelo 'Carrera' en el panel de administración
admin.site.register(Carrera)

# Registra el modelo 'Estudiante' en el panel de administración
admin.site.register(Estudiante)

# Registra el modelo 'Curso' en el panel de administración
admin.site.register(Curso)

# Registra el modelo 'Matricula' en el panel de administración
admin.site.register(Matricula)
