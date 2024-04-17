from django.contrib import admin
from .models import Flan, ContactForm
# Register your models here.
# Se hace para importar todos los modelos , cada vez que se quiera
#importar un nuevo modelo ,se debe hacer la linea respectiva para ese modelo
admin.site.register(Flan)
admin.site.register(ContactForm)