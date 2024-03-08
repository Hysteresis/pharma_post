from app.models import ODS, D_Date, D_Type, D_Geographie, F_Dose
from django.db import transaction

def run():

    # D_Date.objects.all().delete()
    # # D_DATE
    # dates_all = ODS.objects.values_list('date_fin_semaine', flat=True).distinct()
    #
    # dates = []
    #
    # for d in dates_all:
    #     if not D_Date.objects.filter(pk_date=d).exists():
    #         d_date = D_Date(pk_date=d)
    #         dates.append(d_date)
    #     else:
    #         print("doublon")
    # D_Date.objects.bulk_create(dates)
    #
    # # D_TYPE
    # D_Type.objects.all().delete()
    # types_all = ODS.objects.values_list('type_de_vaccin', flat=True).distinct()
    # types = []
    # for t in types_all:
    #     d_type = D_Type(pk=t)
    #     types.append(d_type)
    # D_Type.objects.bulk_create(types)
    # print(types)

    # D_Geographie
    # D_Geographie.objects.all().delete()
    #
    # geographies = []
    #
    # # Récupérer les valeurs distinctes de code_region, libelle_region, code_departement, libelle_departement de l'ODS
    # data = ODS.objects.values('code_region', 'libelle_region', 'code_departement', 'libelle_departement').distinct()
    #
    # for item in data:
    #     code_departement = item['code_departement']
    #     if len(code_departement) == 1:
    #         code_departement = f"0{code_departement}"
    #
    #     pk_geographie = f"{code_departement}-{item['code_region']}"
    #
    #     if not any(geo.pk_geographie == pk_geographie for geo in geographies):
    #         geographie = D_Geographie(
    #             pk_geographie=pk_geographie,
    #             code_region=item['code_region'],
    #             label_region=item['libelle_region'],
    #             code_departement=code_departement,
    #             label_departement=item['libelle_departement']
    #         )
    #         geographies.append(geographie)
    #
    # D_Geographie.objects.bulk_create(geographies)

    # F_Dose
    F_Dose.objects.all().delete()

    data = ODS.objects.all()

    doses = []

    with transaction.atomic():
        for item in data:
            fk_date, _ = D_Date.objects.get_or_create(pk_date=item.date_fin_semaine)
            fk_type, _ = D_Type.objects.get_or_create(pk_type=item.type_de_vaccin)

            code_departement = item.code_departement
            if len(code_departement) == 1:
                code_departement = f"0{code_departement}"

            pk_geographie = f"{code_departement}-{item.code_region}"
            fk_geographie, _ = D_Geographie.objects.get_or_create(pk_geographie=pk_geographie)

            pk_dose = f"{fk_date.pk_date}-{fk_type.pk_type}-{fk_geographie.pk_geographie}"

            if not any(d.pk_dose == pk_dose for d in doses):
                dose = F_Dose(
                    pk_dose=pk_dose,
                    nb_ucd=item.nb_ucd,
                    nb_doses=item.nb_doses,
                    fk_date=fk_date,
                    fk_type=fk_type,
                    fk_geographie=fk_geographie
                )
                print(dose)
                doses.append(dose)
        F_Dose.objects.bulk_create(doses)

