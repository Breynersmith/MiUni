from django.db import models

# Define tus modelos de base de datos

# Modelo para representar Carreras
class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)  # Código único de la carrera
    nombre = models.CharField(max_length=50)  # Nombre de la carrera
    duracion = models.PositiveSmallIntegerField(default=5)  # Duración en años de la carrera (valor predeterminado: 5 años)

    def __str__(self):
        # Devuelve una representación legible de la carrera
        txt = "{0} (duracion: {1} año(s))"
        return txt.format(self.nombre, self.duracion)

# Modelo para representar Estudiantes
class Estudiante(models.Model):
    dni = models.CharField(max_length=11, primary_key=True)  # DNI único del estudiante
    apellidoPaterno = models.CharField(max_length=35)  # Apellido paterno
    apellidoMaterno = models.CharField(max_length=35)  # Apellido materno
    nombres = models.CharField(max_length=50)  # Nombres
    fechaNacimiento = models.DateField()  # Fecha de nacimiento

    # Opciones para el campo 'sexo' con selección de género
    sexos = [('M', 'Masculino'), ('F', 'Femenino')]
    sexo = models.CharField(max_length=1, choices=sexos, default='M')  # Género (por defecto: Masculino)

    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)  # Relación con la carrera
    vigencia = models.BooleanField(default=True)  # Estado de vigencia del estudiante (por defecto: Vigente)

    def nombreCompleto(self):
        # Devuelve el nombre completo del estudiante
        txt = '{0} {1} {2}'
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

    def __str__(self):
        # Devuelve una representación legible del estudiante
        txt = "{0} / carrera: {1} / {2}"
        if self.vigencia:
            estadoEstudiante = 'VIGENTE'
        else:
            estadoEstudiante = 'NO VIGENTE'
        return txt.format(self.nombreCompleto(), self.carrera, estadoEstudiante)

# Modelo para representar Cursos
class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)  # Código único del curso
    nombre = models.CharField(max_length=50)  # Nombre del curso
    creditos = models.PositiveSmallIntegerField()  # Número de créditos del curso
    docente = models.CharField(max_length=100)  # Nombre del docente del curso

    def __str__(self):
        # Devuelve una representación legible del curso
        txt = "{0}  ({1}) / Docente: {2}"
        return txt.format(self.codigo, self.nombre, self.docente)

# Modelo para representar Matrículas
class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)  # Relación con el estudiante
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)  # Relación con el curso
    fechaMatricula = models.DateTimeField(auto_now_add=True)  # Fecha y hora de la matrícula (se autogenera)

    def __str__(self):
        # Devuelve una representación legible de la matrícula
        txt = "{0} matriculado(a) en el curso {2} / Fecha: {1}"
        fechaMatruc = self.fechaMatricula.strftime("%d/%m/%Y %H:%M:%S")  # Formatea la fecha
        return txt.format(self.estudiante, fechaMatruc, self.curso)
