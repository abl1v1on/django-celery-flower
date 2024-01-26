from django import forms
from .models import Contact


class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if Contact.objects.filter(email=email).exists():
            raise forms.ValidationError('Вы уже подписанны на рассылку!')
        return email