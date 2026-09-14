from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets

from .forms import NodoServidorForm, IncidenciaServidorForm
from .models import NodoServidor, RegistroAuditoria, IncidenciaServidor
from .serializers import (
    NodoServidorSerializer,
    RegistroAuditoriaSerializer,
    IncidenciaServidorSerializer,
)

# ==========================================
# VISTAS HTML TRADICIONALES (PLANTILLAS)
# ==========================================

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
    contexto = {'nodo': servidor}
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


# ==========================================
# VISTAS API REST (DJANGO REST FRAMEWORK)
# ==========================================

class NodoServidorViewSet(viewsets.ModelViewSet):
    queryset = NodoServidor.objects.all()
    serializer_class = NodoServidorSerializer

class RegistroAuditoriaViewSet(viewsets.ModelViewSet):
    queryset = RegistroAuditoria.objects.all()
    serializer_class = RegistroAuditoriaSerializer

class IncidenciaServidorViewSet(viewsets.ModelViewSet):
    queryset = IncidenciaServidor.objects.all()
    serializer_class = IncidenciaServidorSerializer


from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import MantenimientoForm
from .models import MantenimientoNodo


class MantenimientoListView(ListView):
    model = MantenimientoNodo
    template_name = 'infraestructura/mantenimiento_list.html'
    context_object_name = 'mantenimientos'


class MantenimientoDetailView(DetailView):
    model = MantenimientoNodo
    template_name = 'infraestructura/mantenimiento_detail.html'
    context_object_name = 'mantenimiento'


class MantenimientoCreateView(CreateView):
    model = MantenimientoNodo
    form_class = MantenimientoForm
    template_name = 'infraestructura/mantenimiento_form.html'
    success_url = reverse_lazy('lista_mantenimientos')


class MantenimientoUpdateView(UpdateView):
    model = MantenimientoNodo
    form_class = MantenimientoForm
    template_name = 'infraestructura/mantenimiento_form.html'
    success_url = reverse_lazy('lista_mantenimientos')


class MantenimientoDeleteView(DeleteView):
    model = MantenimientoNodo
    template_name = 'infraestructura/mantenimiento_confirm_delete.html'
    success_url = reverse_lazy('lista_mantenimientos')