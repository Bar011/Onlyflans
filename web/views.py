from django.shortcuts import render

# Create your views here.
def index(request): # La definición de esta funcion, maneja 
    # la petición que retornará la vista index.htmñ

    return render(request, 'index.html')

def about(request):
    return render (request, 'about.html')

def welcome(request):
    return render (request, 'welcome.html')

