from django.shortcuts import render
from inkamarket.models import Categorias, Productos, Clientes, Empleados, Proveedores, Contactos

def loginPagina(request):
    if request.method=="POST":
        usuario = request.POST["txtusuario"]
        password = request.POST["txtpassword"]
        if usuario == "admin" and password == "1234":
        

            return render(request,'inkamarket/inicio.html')

    return render(request,'inkamarket/login.html')

# ─── INICIO ───
def inicio(request):
    return render(request, 'inkamarket/inicio.html')

# ─── CATEGORIAS ───
def categoriasInicio(request):
    return render(request, 'inkamarket/categorias/categorias.html')

def categoriasAlta(request):
    id     = int(request.POST["txtidcategoria"])
    nombre = request.POST["txtnombre"]
    c      = Categorias()
    try:
        c.alta(id, nombre)
        contexto = {"id":id, "nombre":nombre, "mensaje":"CATEGORIA AÑADIDA CORRECTAMENTE ✅"}
    except:
        contexto = {"id":id, "nombre":nombre, "mensaje":"NO SE PUDO AÑADIR ❌"}
    return render(request, 'inkamarket/categorias/alta.html', contexto)

def categoriasBaja(request):
    id = int(request.POST["txtidcategoria"])
    c  = Categorias()
    try:
        c.baja(id)
        contexto = {"id":id, "mensaje":"CATEGORIA BORRADA CORRECTAMENTE ✅"}
    except:
        contexto = {"id":id, "mensaje":"NO SE ENCONTRO O NO SE PUDO BORRAR ❌"}
    return render(request, 'inkamarket/categorias/baja.html', contexto)

def categoriasModificar(request):
    id     = int(request.POST["txtidcategoria"])
    nombre = request.POST["txtnombre"]
    c      = Categorias()
    c.modificar(id, nombre)
    contexto = {"id":id, "nombre":nombre, "mensaje":"CATEGORIA MODIFICADA CORRECTAMENTE ✅"}
    return render(request, 'inkamarket/categorias/modificar.html', contexto)

def categoriasConsultar(request):
    c      = Categorias()
    cursor = c.consultar()
    contexto = {"lista_categorias":cursor}
    return render(request, 'inkamarket/categorias/consultar.html', contexto)

# ─── PRODUCTOS ───
def productosInicio(request):
    return render(request,'inkamarket/productos/productos.html')

def productosAlta(request):
    id=int(request.POST["txtidproducto"])
    nombre=request.POST["txtnombre"]
    precio=int(request.POST["txtprecio"])
    id_cat=int(request.POST["txtid_categoria"])
    p=Productos()
    try:
        p.alta(id,nombre,precio,id_cat)
        contexto={"id":id,"nombre":nombre,"precio":precio,"id_cat":id_cat,"mensaje":"PRODUCTO AÑADIDO CORRECTAMENTE"}
    except:
        contexto={"id":id,"nombre":nombre,"precio":precio,"id_cat":id_cat,"mensaje":"NO SE AÑADIO NINGUN PRODUCTO"}
    return render(request,'inkamarket/productos/alta.html',contexto)
def productosBaja(request):
    id=int(request.POST["txtidproducto"])
    p=Productos()
    try:
        p.baja(id)
        contexto={"id":id,"mensaje":"PRODUCTO DADO DE BAJA"}
    except:
        contexto={"id":id,"mensaje":"PRODUCTO AUN NO DADO DE BAJA"}
    return render(request,'inkamarket/productos/baja.html',contexto)
def productosConsultar(request):
    #nombre=request.POST["txtnombre"]
    #foto=request.POST["txtfoto"]
    p      = Productos()
    cursor = p.consultar()
    contexto = {"lista_productos":cursor}
    return render(request, 'inkamarket/productos/consultar.html', contexto)

# ─── CLIENTES ───
def clientesInicio(request):
    return render(request, 'inkamarket/clientes/clientes.html')

def clientesAlta(request):
    dni    = request.POST["txtdni"]
    nombre = request.POST["txtnombre"]
    email  = request.POST["txtemail"]
    ciudad = request.POST["txtciudad"]
    c      = Clientes()
    try:
        c.alta(dni, nombre, email, ciudad)
        contexto = {"dni":dni, "nombre":nombre,"email":email,"ciudad": ciudad, "mensaje":"CLIENTE AÑADIDO CORRECTAMENTE ✅"}
    except:
        contexto = {"dni":dni, "nombre":nombre,"email":email,"ciudad":ciudad, "mensaje":"NO SE PUDO AÑADIR ❌"}
    return render(request, 'inkamarket/clientes/alta.html', contexto)

def clientesBaja(request):
    dni = request.POST["txtdni"]
    c   = Clientes()
    try:
        c.baja(dni)
        contexto = {"dni":dni, "mensaje":"CLIENTE BORRADO CORRECTAMENTE ✅"}
    except:
        contexto = {"dni":dni, "mensaje":"NO SE ENCONTRO O NO SE PUDO BORRAR ❌"}
    return render(request, 'inkamarket/clientes/baja.html', contexto)

def clientesModificar(request):
    dni    = request.POST["txtdni"]
    nombre = request.POST["txtnombre"]
    email  = request.POST["txtemail"]
    ciudad = request.POST["txtciudad"]
    c      = Clientes()
    c.modificar(dni, nombre, email, ciudad)
    contexto = {"dni":dni, "nombre":nombre,"email":email,"ciudad":ciudad, "mensaje":"CLIENTE MODIFICADO CORRECTAMENTE ✅"}
    return render(request, 'inkamarket/clientes/modificar.html', contexto)

def clientesConsultar(request):
    c      = Clientes()
    cursor = c.consultar()
    contexto = {"lista_clientes":cursor}
    return render(request, 'inkamarket/clientes/consultar.html', contexto)

# ─── EMPLEADOS ───
def empleadosConsultar(request):
    e      = Empleados()
    cursor = e.consultar()
    contexto = {"lista_empleados":cursor}
    return render(request, 'inkamarket/empleados.html', contexto)

# ─── PROVEEDORES ───
def proveedoresConsultar(request):
    p      = Proveedores()
    cursor = p.consultar()
    contexto = {"lista_proveedores":cursor}
    return render(request, 'inkamarket/proveedores.html', contexto)

# ─── CONTACTOS ───
def contactosInsertar(request):
    contexto = {}  # Empezamos con el diccionario vacío

    # Aquí, como el action te deja en el mismo sitio, la función se ejecuta siempre, y por eso necesitas el IF para separar el momento de "ver" del momento de "guardar".
    if request.method == "POST": # Como te quedas en la misma URL, la función se ejecuta tanto para "mostrar" la página como para "guardar" los datos.
        try:
            id = int(request.POST["txtidcontacto"])
            nombre = request.POST["txtnombre"]
            email = request.POST["txtemail"]
            mensaje = request.POST["txtmensaje"]
            tipo = request.POST["txttipo"]

            c = Contactos()

            c.insertar(id, nombre, email, mensaje, tipo)
            contexto = {"mensaje": "MENSAJE ENVIADO CORRECTAMENTE ✅"}
        except:
            contexto = {"mensaje": "NO SE PUDO ENVIAR ❌"}

    # Si no es POST (o sea, si solo están entrando a ver),
    # se salta lo de arriba y viene directo aquí:
    return render(request, 'inkamarket/contactos.html', contexto)


    
