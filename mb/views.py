from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.

def home(request):
    context = 'river'
    return render(request, "home.html", {'context': context})

def sendmail(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
    asunto= 'Confirmación de Compra'
    cuerpo = 'Gracias por tu compra. Hemos enviado un correo de confirmación a tu dirección: ' + 'correo_destinatario'
    mensaje = f'{cuerpo}Si no recibes el correo, por favor comunícate con nosotros por WhatsApp al número +123456789.'
    cel = '11-2394-1223'
    
    subject = asunto
    message = mensaje
    from_email = 'notificaciondepaginaweb@gmail.com'
    recipient_list = ['notificaciondepaginaweb@gmail.com','maximobatallan@gmail.com']

    correo= 'correo@correo.com'
    
    send_mail(subject, message, from_email, recipient_list)