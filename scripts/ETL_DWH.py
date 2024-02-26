from app.models import ODS, D_Date, D_Type


def run():

    D_Date.objects.all().delete()
    # D_DATE
    dates_all = ODS.objects.values_list('date_fin_semaine', flat=True).distinct()

    dates = []

    for d in dates_all:
        if not D_Date.objects.filter(pk_date=d).exists():
            d_date = D_Date(pk_date=d)
            dates.append(d_date)
        else:
            print("doublon")
    D_Date.objects.bulk_create(dates)

    # D_TYPE
    D_Type.objects.all().delete()
    types_all = ODS.objects.values_list('type_de_vaccin', flat=True).distinct()

    types = []
    for t in types_all:
        d_type = D_Type(pk=t)
        types.append(d_type)

    D_Type.objects.bulk_create(types)
    print(types)
