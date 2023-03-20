from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ContactForm


def home_page(request):
    return render(request, 'index.html')


@login_required
def contact_page(request):
    if request.method == 'POST':
        email = request.user.email
        contact_form = ContactForm(request.POST, initial={'email': email})
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.info(request, "Thank you, Your message has been sent")
        return render(request, 'message-received.html')
    else:
        email = request.user.email
        contact_form = ContactForm(initial={'email': email})
    context = {
        'contact_form': contact_form
    }
    return render(request, 'contact-us.html', context)
