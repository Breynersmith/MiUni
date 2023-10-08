# Importa las configuraciones de Django desde settings.py
from django.conf import settings
# Importa la función 'render' para renderizar plantillas HTML
from django.shortcuts import redirect, render
# Importa la función 'send_mail' para enviar correos electrónicos
from django.core.mail import send_mail
from .formularios import EstudianteForm, CarreraForm, CursoForm, MatriculaForm
from .models import Estudiante, Carrera, Curso, Matricula

# Define las vistas de tu aplicación

# Vista para la página de inicio
def Home(request):

    estudianteDB = Estudiante.objects.all()
    carreraDB = Carrera.objects.all()
    cursoDB = Curso.objects.all()
    matriculaDB = Matricula.objects.all()

    # Renderiza la plantilla 'home.html' y la muestra en el navegador
    return render(request, 'home.html', {'estudianteDB': estudianteDB, 'carreraDB': carreraDB, 'cursoDB': cursoDB, 'matriculaDB': matriculaDB})

# Vista para el formulario de contacto
def formularioContacto(request):
    # Renderiza la plantilla 'formContacto.html' y la muestra en el navegador
    return render(request, 'formContacto.html')

# Vista para procesar el formulario de contacto
def contactar(request):
    # Verifica si la solicitud HTTP es un POST (cuando se envía el formulario)
    if request.method == 'POST':
        # Obtiene los datos del formulario mediante request.POST
        nombre = request.POST['nombre']
        asunto = request.POST['asunto']
        # Combina el mensaje del usuario con su dirección de correo electrónico
        mensaje = request.POST['mensaje'] + " / Email: " + request.POST['email']
        # Obtiene la dirección de correo electrónico de origen desde la configuración de Django
        origen_email = settings.EMAIL_HOST_USER
        # Define una lista de direcciones de correo electrónico de destino
        destino_email = ['breynersmithustariz@gmail.com', request.POST['email']]
        # Envía el correo electrónico con los datos proporcionados
        send_mail(asunto, mensaje, origen_email, destino_email, fail_silently=False)
        # Renderiza la plantilla 'contactoExitoso.html' para mostrar un mensaje de éxito
        return render(request, 'contactoExitoso.html')
    
    # Si la solicitud no es un POST, vuelve a mostrar el formulario
    return render(request, 'formContacto.html')

def Estudiantes(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estudiantes')
    else:
        form = EstudianteForm()
    estudianteDB = Estudiante.objects.all()
    return render(request, 'estudiantes.html', {'estudianteDB': estudianteDB, 'form': form})


def Carreras(request):
    if request.method == 'POST':
        form = CarreraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carreras')
    else:
        form = CarreraForm()

    carreraDB = Carrera.objects.all()
    return render(request, 'carreras.html', {'carreraDB': carreraDB, 'form': form})

def Cursos(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = CursoForm()
    cursoDB = Curso.objects.all()
    return render(request, 'cursos.html', {'cursoDB': cursoDB, 'form': form})

def Matriculas(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matriculas')
    else:
        form = MatriculaForm()
    matriculaDB = Matricula.objects.all()
    return render(request, 'matriculas.html', {'matriculaDB': matriculaDB, 'form': form})

