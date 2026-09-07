from django.shortcuts import render, redirect, get_object_or_404
from.forms import NodoServidorForm, IncidenciaServidorForm
from .models import NodoServidor, IncidenciaServidor

def eliminar_servidor(request, pk):
    nodo = get_object_or_404(NodoServidor, pk=pk)
    if request.method == 'POST':
        nodo.delete()
        return redirect('home_servidores')
    return render(request, 'infraestructura/eliminar_servidor.html', {'nodo': nodo})

def editar_servidor(request, pk):
    nodo = get_object_or_404(NodoServidor, pk=pk)
    if request.method == 'POST':
        form = NodoServidorForm(request.POST, instance=nodo)
        if form.is_valid():
            form.save()
            return redirect('detalle_servidor', pk=nodo.pk)
    else:
        form = NodoServidorForm(instance=nodo)
    return render(request, 'infraestructura/editar_servidor.html', {'form': form, 'nodo': nodo})

def crear_servidor(request):
    if request.method == 'POST':
        form = NodoServidorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_servidores')
    else:
        form = NodoServidorForm()
    return render(request, 'infraestructura/crear_servidor.html', {'form': form})

def detalle_servidor(request, pk):
	servidor = get_object_or_404(NodoServidor, pk=pk)
	contexto = {'nodo' : servidor}
	return render(request, 'infraestructura/detalle.html', contexto)

def lista_servidores(request):
	servidores = NodoServidor.objects.all()
	contexto = {'servidores': servidores}
	return render(request, 'infraestructura/index.html', contexto)

def crear_incidencia(request, pk):
    servidor = get_object_or_404(NodoServidor, pk=pk)
    if request.method == 'POST':
        form = IncidenciaServidorForm(request.POST)
        if form.is_valid():
            incidencia = form.save(commit=False)
            incidencia.servidor = servidor
            incidencia.save()
            return redirect('detalle_servidor', pk=servidor.pk)
    else:
        form = IncidenciaServidorForm()
    contexto = {'form': form, 'nodo': servidor}
    return render(request, 'infraestructura/crear_incidencia.html', contexto)


def resolver_incidencia(request, pk):
    incidencia = get_object_or_404(IncidenciaServidor, pk=pk)
    incidencia.resuelta = True
    incidencia.save()
    return redirect('detalle_servidor', pk=incidencia.servidor.pk)