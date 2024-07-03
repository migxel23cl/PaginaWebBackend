from django.shortcuts import render

# Create your views here.
def index(request):    
    return render(request,"index.html")


def login(request):
    return render(request,"login.html")

def registro(request):
    return render(request,"registro.html")

def gusto(request):
    return render(request,"gustos.html")

def productos(request):
    return render(request,"productos.html")

def productoU(request):
    return render(request,"productoU.html")

def ventanaPago(request):
    return render(request,"ventanaPago.html")





