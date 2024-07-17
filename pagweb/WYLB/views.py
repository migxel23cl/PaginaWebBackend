from django.shortcuts import render, redirect
from .models import Usuario, Producto
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm
#from .forms import ProductoForm


# Create your views here.
def index(request):    
    return render(request,"index.html")

def quepjeres(request):
    return render(request, "quepjeres.html")


def login(request):
    return render(request,"login.html")

def registro(request):
        return render(request, "registro.html",)
    

def crud(request):
    usuarios = Usuario.objects.all()
    context = {
        "usuarios": usuarios,
    }
    return render(request, "crud.html", context)


def gusto(request):
    return render(request,"gustos.html")


def feed(request):
    return render (request,"feed.html")

def productoU(request):
    return render(request,"productoU.html")

def ventanaPago(request):
    return render(request,"ventanaPago.html")


def user_findEdit(request,pk):
    if pk!="":
        """ 
            objects.get() = Obtener datos con filtro
            objects.all() = Obtener todos
        """
        usuario = Usuario.objects.get(id=pk)

        context={
            "usuario":usuario,
        }
        return render(request,"user_update.html",context)
    else:
        usuarios = Usuario.objects.all()
        context={
            "mensaje":"Error,correo no encontrado",
            "usuarios":usuarios
        }
        return render(request,"crud.html",context)
    

def user_update(request):
    if request.method=="POST":
        """ 
            Capturo todos los datos del front
            Identificamos
            Asignamos nombre 
        """
        nombre = request.POST["nombre"]
        apellido = request.POST["appPaterno"]
        correo = request.POST["correo"]
        password = request.POST["password"]


        obj = Usuario(
            nombre=nombre,
            apellido=apellido,
            email=correo,
            password=password,
        )
        obj.save()

        Usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Modificado con Exito",
            "usuario":Usuarios,
        }
        return render(request, "user_update.html", context)

def conectar(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            usuarios = Usuario.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"crud.html",context)
        else:
            context = {
                "mensaje":"Usuario o contraseña incorrecta",
            }
            return render(request,"login.html",context)
    else:
        context = {

        }
        return render(request,"login.html",context)
    


def product_list(request):
    products = Producto.objects.all()
    return render(request, 'product_list.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductoForm()
    return render(request, 'add_product.html', {'form': form})



def perfil(request):
    return render(request, "perfil.html")

def lista_productos(request):
    products = Producto.objects.all()
    return render(request, 'productos.html', {'products': products})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})