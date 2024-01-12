from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import CarrosForm
from app.models import Carros

# Create your views here.
def home(request):
    data = {}
    data['dado'] = Carros.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)

def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['dados'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit (request, pk):
    data = {}
    data ['dados'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['dados'])
    return render(request, 'form.html', data)

def update (request, pk):
    data = {}
    data['dados'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['dados'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    dados = Carros.objects.get(pk=pk)
    dados.delete()
    return redirect('home')