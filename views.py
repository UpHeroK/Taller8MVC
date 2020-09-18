
from django.shortcuts import render, redirect
from .models import*
from .forms import CiudadForm, PersonaForm, DocumentoForm

def home(request):
    return render(request,'aplicacion/index.html')

def crearCiudad(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CiudadForm()
    return render(request,'aplicacion/CrearCiudad.html', {'form':form})


def listarCiudad(request):
    Ciudad = ciudad.objects.all()
    context={'Ciudad':Ciudad}
    return  render(request,'aplicacion/ListarCiudad.html',context)

def editarCiudad(request, id):
    editCiudad = ciudad.objects.get(idciudad = id)
    if request.method == 'GET':
        form = CiudadForm(instance = editCiudad)
    else:
        form = CiudadForm(request.POST, instance = editCiudad)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'aplicacion/CrearCiudad.html', {'form':form})

def eliminarCiudad (request, id):
    elimCiudad = ciudad.objects.get(idciudad = id)
    if request.method == 'POST':
        elimCiudad.delete()
        return redirect('index')
    return render(request,'aplicacion/EliminarCiudad.html', {'elimCiudad':elimCiudad})

def crearPersona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PersonaForm()
    return render(request,'aplicacion/CrearPersona.html', {'form':form})


def listarPersona(request):
    Persona = persona.objects.all()
    context={'Persona':Persona}
    return  render(request,'aplicacion/ListarPersona.html',context)

def editarPersona(request, id):
    editPersona = persona.objects.get(idp = id)
    if request.method == 'GET':
        form = PersonaForm(instance = editPersona)
    else:
        form = PersonaForm(request.POST, instance = editPersona)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'aplicacion/CrearPersona.html', {'form':form})

def eliminarPersona (request, id):
    elimPersona = persona.objects.get(idp = id)
    if request.method == 'POST':
        elimPersona.delete()
        return redirect('index')
    return render(request,'aplicacion/EliminarPersona.html', {'elimPersona':elimPersona})

def crearDocumento(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentoForm()
    return render(request,'aplicacion/CrearDocumento.html', {'form':form})

def listarDocumento(request):
    Documento = documento.objects.all()
    context = {'Documento': Documento}
    return render(request,'aplicacion/ListarDocumento.html',context)

def eliminarDocumento (request, id):
    elimDocumento = documento.objects.get(idoc = id)
    if request.method == 'POST':
        elimDocumento.delete()
        return redirect('index')
    return render(request,'aplicacion/EliminarDocumento.html', {'elimDocumento':elimDocumento})

def editarDocumento(request, id):
    editDocumento = documento.objects.get(idoc = id)
    if request.method == 'GET':
        form = DocumentoForm(instance = editDocumento)
    else:
        form = DocumentoForm(request.POST, instance = editDocumento)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'aplicacion/CrearDocumento.html', {'form':form})

# Create your views here.
