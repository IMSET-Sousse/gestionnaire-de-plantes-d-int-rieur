from django.shortcuts import render, redirect
from .models import Plante
from .forms import PlanteForm

def ajouter_plante(request):
    if request.method == 'POST':
        form = PlanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_plantes')
    else:
        form = PlanteForm()
    return render(request, 'ajouter_plante.html', {'form': form})

def list_plantes(request):
    plantes = Plante.objects.all()
    return render(request, 'list_plantes.html', {'plantes': plantes})
