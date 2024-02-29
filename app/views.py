from django.shortcuts import render

from app.models import F_Dose


# Create your views here.
def index(request):
    data_F_Dose = F_Dose.objects.all()
    nombre_lignes_F_Dose = F_Dose.objects.count()
    context = {
        'data_F_Dose': data_F_Dose,
        'nombre_lignes_F_Dose': nombre_lignes_F_Dose,
        'request': request}
    return render(request, 'index.html', context=context)