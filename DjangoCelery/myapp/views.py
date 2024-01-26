from django.shortcuts import render
from django.views.generic import CreateView

from .forms import CreateContactForm
from .models import Contact
from .service import send
from .tasks import send_spam_mail


class ContactView(CreateView):
    form_class = CreateContactForm
    model = Contact
    success_url = '/'
    template_name = 'index.html'

    def form_valid(self, form):
        form.save()
        send_spam_mail.delay(form.instance.email)
        return super().form_valid(form)
