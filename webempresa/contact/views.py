from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
	contact_form = ContactForm()
	if request.method == 'POST':
		contact_form = ContactForm(data=request.POST)

		if contact_form.is_valid():
			name = request.POST.get('name', '')
			email = request.POST.get('email', '')
			content = request.POST.get('content', '')
			# Enviamos el correo y redireccionamos 
			email = EmailMessage(
				# Asunto
				"La Caffettiera: Nuevo mensaje de contacto",
				# Cuerpo
				"De {} <{}>\n\nEscribió: {}".format(name, email, content),
				# email_origen,
				"no-reply@inbox.mailtrap.io",
				# email(s) de destino
				["marcelpm1987@gmail.com"],
				reply_to=[email]
			)

			try:
				email.send()
				# si todo ha ido bien, redireccionamos a ok
				return redirect(reverse('contact')+"?ok")
			except:
				# Si algo falla, redirecionamos a fail
				return redirect(reverse('contact')+"?fail")

	return render(request, "contact/contact.html", {'form':contact_form})