# Importa las configuraciones de Django desde settings.py
from django.conf import settings
# Importa la función 'render' para renderizar plantillas HTML
from django.shortcuts import render
# Importa la función 'send_mail' para enviar correos electrónicos
from django.core.mail import send_mail

# Define las vistas de tu aplicación

# Vista para la página de inicio
def home(request):
    # Renderiza la plantilla 'home.html' y la muestra en el navegador
    return render(request, 'home.html')

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