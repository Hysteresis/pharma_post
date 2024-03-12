# import requests
from app.models import F_Dose, D_Date
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    data_F_Dose = F_Dose.objects.all()
    nombre_lignes_F_Dose = F_Dose.objects.count()
    context = {
        'data_F_Dose': data_F_Dose,
        'nombre_lignes_F_Dose': nombre_lignes_F_Dose,
        'request': request}
    return render(request, 'index.html', context=context)

def date(request):
    dates_list = D_Date.objects.all().order_by('pk_date')
    paginator = Paginator(dates_list, 10)

    page = request.GET.get('page')
    # try:
    dates = paginator.page(page)
    # except EmptyPage:
    #     dates = paginator.page(paginator.num_pages)

    return render(request, 'date.html', {'dates': dates})
