from django.shortcuts import render
from django.http import HttpResponse
from app.forms import CarrosForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)