from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form = ContactForm
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            content = request.POST['content']
            # Enviamos el correo y direccionamos
            email = EmailMessage(
                "La cafetiera",
                f"De {name} <{email}>\n\nEscribió:\n\n{content}",
                "no-contestar@inbox.mailtrap.io",
                ["alexis.rj2110@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien
                return redirect(reverse('contact')+"?fail")
            
    return render(request, "contact/contact.html", {'form':contact_form})