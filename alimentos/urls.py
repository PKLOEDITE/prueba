from django.urls import path, include
from .import views
urlpatterns = [
    path('index',views.index, name='index'),
    path('listar', views.listar, name="listar"),
    path('buscar', views.buscar, name="buscar"),
    path('buscar_por_rut', views.buscar_por_rut, name="buscar_por_rut"),
    path('eliminar', views.eliminar, name="eliminar"),
    path('eliminar_por_rut', views.eliminar_por_rut, name="eliminar_por_rut"),
    path('agregarP', views.agregarP, name="agregarP"),
    path('agregar_persona',views.agregarPerson,name="agregar_persona"),
    path('agregarA', views.agregarA, name="agregarA"),
    path('agregar_admin',views.agregarAdmin,name="agregar_admin"),
    path('editar', views.editar, name="editar"),
    path('buscar_para_editar',views.buscar_para_editar,name="buscar_para_editar"),
    path('actualizar_persona',views.actualizar_persona, name="actualizar_persona"),


    path('menu',views.menu,name="menu"),
    path('contacto',views.contacto,name="contacto"),
    path('agregarform',views.agregarform, name="agregarform"),
    path('formulario',views.formulario,name="formulario"),
    path('c_ave',views.c_ave,name="c_ave"),
    path('c_gato',views.c_gato,name="c_gato"),
    path('c_hamster',views.c_hamster,name="c_hamster"),
    path('c_perro',views.c_perro,name="c_perro"),
    path('c_tortuga',views.c_tortuga,name="c_tortuga"),
]
