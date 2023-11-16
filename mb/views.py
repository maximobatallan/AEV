from django.shortcuts import render
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from .models import formulario


# Create your views here.

def home(request):
    context = 'river'
    return render(request, "home.html", {'context': context})

def send_user_data_email(user_data):
    subject = 'Nuevo usuario registrado'
    message = f'Nuevo Usuario:\n\n{user_data}'
    

    from_email = 'notificaciondepaginaweb@gmail.com'
    recipient_list = ['notificaciondepaginaweb@gmail.com','maximobatallan@gmail.com']
    send_mail(subject, message, from_email, recipient_list)


@csrf_exempt
def save_formulario(request):
    

    nombre = request.POST.get('nombre')

    telefono = request.POST.get('telefono')
    email = request.POST.get('email')
    texto = request.POST.get('texto')
    categoria = request.POST.get('categoria')
    
    
    formulario1 = formulario(nombre=nombre, categoria=categoria, telefono=telefono, mail=email, texto=texto)
    formulario1.save()
    user_data = f"nombre: {nombre} telefono: {telefono} categoria: {categoria} texto: {texto}"
    send_user_data_email(user_data)
    
    
    
    return render(request, 'home.html')


def asistentevirtual(request):    
    
    return render(request, 'asistentevirtual.html')

def desarrollospersonalizados(request):    
    
    return render(request, 'desarrollospersonalizados.html')

def exposicionenlinea(request):    
    
    return render(request, 'exposicionenlinea.html')

def gestiondelainformacion(request):    
    
    return render(request, 'gestiondelainformacion.html')