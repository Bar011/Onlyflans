from django import forms 
from .models import ContactForm

# Create the form class.

#Esto es para utilizar el form nativo de django
#class ContactFormForm(forms.Form):
    #customer_email = forms.EmailField(label= 'correo')
    #customer_name = forms.CharField(label= 'nombre')
    #message = forms.CharField(label= 'mensaje')

#Es para poder utilizar el modelo en base de datos, es mas facil de manejar
#Esto es para utilizar el modelo desde la base de datos como formulario y no el nativo de django
class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        labels = {
            'customer_email': 'Correo electrónico',
            'customer_name': 'Nombre',
            'message': 'Mensaje'}