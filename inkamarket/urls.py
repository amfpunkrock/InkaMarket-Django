from django.urls import path
from inkamarket import views

urlpatterns = [

    path('',views.loginPagina,name='login'),
    # INICIO
    path('inicio/', views.inicio, name="inicio"),

    # CATEGORIAS
    path('categorias/',           views.categoriasInicio,    name="categorias"),
    path('categorias/alta/',      views.categoriasAlta,      name="categoriasAlta"),
    path('categorias/baja/',      views.categoriasBaja,      name="categoriasBaja"),
    path('categorias/modificar/', views.categoriasModificar, name="categoriasModificar"),
    path('categorias/consultar/', views.categoriasConsultar, name="categoriasConsultar"),

    # PRODUCTOS
    path('productos/',views.productosInicio,name="productos"),
    path('productos/alta/',views.productosAlta,name="productosAlta"),
    path('productos/baja/',views.productosBaja,name="productosBaja"),
    path('productos/consultar/', views.productosConsultar, name="productosConsultar"),

    # CLIENTES
    path('clientes/',             views.clientesInicio,      name="clientes"),
    path('clientes/alta/',        views.clientesAlta,        name="clientesAlta"),
    path('clientes/baja/',        views.clientesBaja,        name="clientesBaja"),
    path('clientes/modificar/',   views.clientesModificar,   name="clientesModificar"),
    path('clientes/consultar/',   views.clientesConsultar,   name="clientesConsultar"),

    # EMPLEADOS
    path('empleados/',   views.empleadosConsultar,   name="empleados"),

    # PROVEEDORES
    path('proveedores/', views.proveedoresConsultar, name="proveedores"),

    # CONTACTOS
    path('contactos/',   views.contactosInsertar,    name="contactos"),
]


