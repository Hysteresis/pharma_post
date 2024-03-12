# import requests
from django.db.models import Sum

from app.models import F_Dose, D_Date, D_Geographie
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import timedelta, datetime
from django.shortcuts import redirect
from django.urls import reverse
from django.http import Http404
from app.models import D_Date

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


def find_next_date(request):
    if request.method == 'GET':
        current_date = request.GET.get('current_date')
        if current_date:
            try:
                current_date = datetime.strptime(current_date, '%Y-%m-%d').date()
            except ValueError:
                error_message = "La date saisie n'est pas valide."
                return render(request, 'next_date.html', {'message': error_message})

            next_date = D_Date.objects.filter(pk_date__gt=current_date).order_by('pk_date').first()

            if next_date:
                geographies_starting_with_63 = D_Geographie.objects.filter(pk_geographie__startswith='63').values_list('pk_geographie', flat=True)
                doses_for_next_date = F_Dose.objects.filter(fk_date=next_date, fk_geographie__in=geographies_starting_with_63)
                total_doses_for_next_date = doses_for_next_date.aggregate(total_doses=Sum('nb_doses'))['total_doses'] or 0

                return render(request, 'next_date.html', {'next_date': next_date,
                                                           'total_doses_for_next_date': total_doses_for_next_date})
            else:
                return render(request, 'next_date.html', {'message': 'Aucune date suivante trouvée.'})
        else:
            return render(request, 'next_date.html', {'message': 'Veuillez saisir une date.'})
    else:
        return redirect(reverse('date'))


