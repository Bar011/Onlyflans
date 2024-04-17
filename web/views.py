from django.shortcuts import redirect, render
from .models import Flan
from .forms import ContactFormForm
# Create your views here.
def index(request): # La definición de esta funcion, maneja 
    # la petición que retornará la vista index.htmñ
    flanes_publicos = Flan.objects.filter(is_private= False) #Llamamos al flan
    #Los filtramos si no son privados
    return render(request, 'index.html', {'flanes': flanes_publicos})
    #Los pasamos por contexto
def about(request):
    return render (request, 'about.html')

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private= True)
    return render (request, 'welcome.html', {'flanes': flanes_privados})

def contact(request):
    #Validación del formulario
    if request.method =='POST': #Si el request entra como un post
        form = ContactFormForm(request.POST)#Se instancia el formulario
        if form.is_valid(): #Si el formulario es válido
            form.save() #Se guarda en el modelo. 
            return redirect('success') #Redirecciona a una página de exito
    else: #Si no es un metodo post... 
        form = ContactFormForm() #Va a mostrarlo de nuevo para que se llene correctamente
    return render(request, 'contact.html', {'form' : form})

def success(request):
    return render (request, 'success.html')