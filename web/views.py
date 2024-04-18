from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Flan
from .forms import ContactFormForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request): # La definición de esta funcion, maneja 
    # la petición que retornará la vista index.htmñ
    flanes_publicos = Flan.objects.filter(is_private= False) #Llamamos al flan
    #Los filtramos si no son privados
    return render(request, 'index.html', {'flanes': flanes_publicos})
    #Los pasamos por contexto#
    
#Intento de barra de busqueda de flanes públicos    
def flan_search(request):
    buscador = None
    flanes_publicos = None
    if request.method == 'POST':
            #'buscador' guarda el valor ingresado en el formulario de búsqueda.
            buscador = request.POST['buscador']
            buscador = buscador.lower()
            # Filtrar los distintos objetos flanes para que coincidan con nuestro
            # criterio de búsqueda. En este caso, con el nombre de cada flan.
            flanes_publicos = Flan.objects.filter(name__icontains=buscador, is_private =False)
            return render(request, 'results_search.html', {'flanes': flanes_publicos})
    
def about(request):
    return render (request, 'about.html')

@login_required 
#Esto es un decorador, que nos permite que la vista solo se pueda ver si el usuario está logueado
#Cuidado , si estamos con las credenciales del admin, esto parecerá que no funciona, debemos 
#desloguarnos del admin para poder ver la funcionalidad de esto. 
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

def flan_detail(request,flan_id):
    flan = get_object_or_404(Flan,pk = flan_id)
    return render(request, 'flan_detail.html', {'flan': flan})
    

#Usando las clases de django
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    
class CustomLogoutView(LogoutView):
    next_page = '/'
    