from django.shortcuts import render
from .models import Persona
# Create your views here.
def index(request):
    print("hola estoy en la vista index")
    context={}
    return render (request,'CRUD/index.html',context)

def listar(request):
    print("hola estoy en la vista listar ")
    personas=Persona.objects.all()
    context={'personas':personas}
    return render (request,'CRUD/mostrar_datos.html', context)


def buscar(request):
    print("hola estoy en la vista buscar ")
    context={}
    return render (request,'CRUD/buscar.html', context)


def buscar_por_rut(request):
    print("hola estoy en la vista buscar por rut  ")
    mi_rut=request.POST['rut']
    persona =Persona.objects.get(rut = mi_rut)
    context={'persona':persona}
    return render (request,'CRUD/datos_cliente.html', context)

def eliminar(request):
    print("hola estoy en la vista buscar")
    context={}
    return render(request, 'CRUD/boton_eliminar.html', context)

def eliminar_por_rut(request):
    print("hola estoy en la vista eliminar_por_rut")
    # delete from alumno where rut = mi_rut
    mi_rut = request.POST['rut']
    persona = Persona.objects.get(rut = mi_rut)
    persona.delete()
    context={}
    return render(request, 'mensajes/mensaje_persona_eliminada.html', context)

def agregarP(request):
    print("hola estoy en la vista agregar")
    context={}
    return render(request, 'CRUD/agregar_persona.html', context)

def agregarPerson(request):
    print("hola  estoy en agregar persona...")
    if request.method == 'POST':
       mi_rut = request.POST['rut']
       mi_nombre= request.POST['nombre']
       mi_apellidos=request.POST['apellidos']
       mi_email=request.POST['email']
       mi_direccion =request.POST['direccion']
       mi_cargo=request.POST['cargo']
       mi_comuna = request.POST['comuna']
       mi_telefono = request.POST['telefono']
       mi_tipo = request.POST['tipo']
       if mi_rut != "":
           try:
               persona = Persona()

               persona.rut = mi_rut
               persona.nombre = mi_nombre
               persona.apellidos = mi_apellidos
               persona.email = mi_email
               persona.direccion = mi_direccion
               persona.cargo = mi_cargo
               persona.comuna = mi_comuna
               persona.telefono = mi_telefono
               persona.tipo = mi_tipo

               persona.save()

               return render(request, 'mensajes/datos_agregados.html',{})

           except persona.DoesNotExist:
               return render(request, 'error/error_204.html', {})
       else:
           return render(request, 'error/error_201.html', {})
    else:
        return render(request, 'error/error_203.html', {})


def agregarA(request):
    print("hola estoy en la vista agregar")
    context={}
    return render(request, 'CRUD/agregar_admin.html', context)

def  agregarAdmin(request):
    print("LLenar formuliario de usuario que desea  agregar")
    if request.method == 'POST':
        mi_rut = request.POST['rut']
        mi_nombre = request.POST['nombre']
        mi_apellidos = request.POST['apellidos']
        mi_email = request.POST['email']
        mi_direccion = request.POST['direccion']
        mi_cargo = request.POST['cargo']
        mi_comuna = request.POST['comuna']
        mi_telefono = request.POST['telefono']
        mi_tipo = request.POST['tipo']
        if mi_rut!="":
            try:
                persona = Persona()


                persona.rut = mi_rut
                persona.nombre = mi_nombre
                persona.apellidos = mi_apellidos
                persona.email = mi_email
                persona.direccion = mi_direccion
                persona.cargo = mi_cargo
                persona.comuna = mi_comuna
                persona.telefono = mi_telefono
                persona.tipo = mi_tipo


                persona.save()

                return render(request, 'mensajes/datos_agregados.html', {})

            except persona.DoesNotExist:
                 return render(request, 'error/error_204.html', {})
        else:
            return render(request, 'error/error_201.html', {})
    else:
        return render(request, 'error/error_203.html', {})



def editar(request):
    print("hola estoy en la vista editar")
    context={}
    return render(request, 'CRUD/boton_editar.html', context)

def buscar_para_editar(request):
    print("hola estoy en la vista buscar por rut  ")
    mi_rut=request.POST['rut']
    persona =Persona.objects.get(rut = mi_rut)
    context={'persona':persona}
    return render (request,'CRUD/formulario_editar.html', context)

def  actualizar_persona(request):
    print("LLenar formuliario de usuario que desea  actualizar")
    if request.method == 'POST':
        mi_id =request.POST['id_persona']
        mi_rut = request.POST['rut']
        mi_nombre = request.POST['nombre']
        mi_apellidos = request.POST['apellidos']
        mi_email = request.POST['email']
        mi_direccion = request.POST['direccion']
        mi_cargo = request.POST['cargo']
        mi_comuna = request.POST['comuna']
        mi_telefono = request.POST['telefono']
        mi_tipo = request.POST['tipo']
        if mi_rut!="":
            try:
                persona = Persona()

                persona.id_persona=mi_id
                persona.rut = mi_rut
                persona.nombre = mi_nombre
                persona.apellidos = mi_apellidos
                persona.email = mi_email
                persona.direccion = mi_direccion
                persona.cargo = mi_cargo
                persona.comuna = mi_comuna
                persona.telefono = mi_telefono
                persona.tipo = mi_tipo


                persona.save()

                return render(request, 'mensajes/datos_actualizados.html', {})

            except persona.DoesNotExist:
                 return render(request, 'error/error_204.html', {})
        else:
            return render(request, 'error/error_201.html', {})
    else:
        return render(request, 'error/error_203.html', {})

def menu (request):
    context={}
    return render(request, 'alimentos/menu_prin.html', context)

def contacto (request):
    context={}
    return render(request, 'alimentos/contacto.html', context)

def formulario (request):
    context={}
    return render(request, 'alimentos/formulario.html', context)

def agregarform(request):
    print("hola  estoy en agregar persona...")
    if request.method == 'POST':
       mi_rut = request.POST['rut']
       mi_nombre= request.POST['nombre']
       mi_apellidos=request.POST['apellidos']
       mi_email=request.POST['email']
       mi_direccion =request.POST['direccion']
       mi_cargo=request.POST['cargo']
       mi_comuna = request.POST['comuna']
       mi_telefono = request.POST['telefono']
       mi_tipo = request.POST['tipo']
       if mi_rut != "":
           try:
               persona = Persona()

               persona.rut = mi_rut
               persona.nombre = mi_nombre
               persona.apellidos = mi_apellidos
               persona.email = mi_email
               persona.direccion = mi_direccion
               persona.cargo = mi_cargo
               persona.comuna = mi_comuna
               persona.telefono = mi_telefono
               persona.tipo = mi_tipo

               persona.save()

               return render(request, 'mensajes/datos_agregados.html',{})

           except persona.DoesNotExist:
               return render(request, 'error/error_204.html', {})
       else:
           return render(request, 'error/error_201.html', {})
    else:
        return render(request, 'error/error_203.html', {})



def c_ave (request):
    context={}
    return render(request, 'alimentos/comida_ave.html', context)

def c_gato (request):
    context={}
    return render(request, 'alimentos/comida_gato.html', context)

def c_hamster (request):
    context={}
    return render(request, 'alimentos/comida_hamster.html', context)

def c_perro (request):
    context={}
    return render(request, 'alimentos/comida_perro.html', context)

def c_tortuga (request):
    context={}
    return render(request, 'alimentos/comida_tortugas.html', context)