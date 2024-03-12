import os

from app.models import ODS
import pandas as pd

from pharma_post.settings import DATA_DIR


def run():
    """
    script pour insérer les données dans mon ETL_ODS
    """
    ODS.objects.all().delete()
    file_name = f"flux-total-dep.csv"
    csv_file_path = os.path.join(DATA_DIR, file_name)
    df = pd.read_csv(csv_file_path, sep=',', encoding='ISO-8859-1')
    # df = df.where(pd.notnull(df), None)

    ods_objects = []
    for index, row in df.iterrows():
        nb_ucd = row['nb_ucd']
        nb_doses = row['nb_doses']
        if pd.isna(nb_doses):
            print(f"Valeur non saisie détectée : {nb_doses}")
        # if pd.isnull(nb_ucd):

        #     nb_ucd = None
        # if pd.isnull(nb_doses):
        #     nb_doses = None
        ods = ODS(
            code_region=row['code_region'],
            libelle_region=row['libelle_region'],
            code_departement=row['code_departement'],
            libelle_departement=row['libelle_departement'],
            date_fin_semaine=row['date_fin_semaine'],
            type_de_vaccin=row['type_de_vaccin'],
            nb_ucd=row['nb_ucd'],
            nb_doses=row['nb_doses'],
        )
        ods_objects.append(ods)
    # for elt in ods_objects:
    #     # print(elt.nb_doses)
    #     if not isinstance(elt.nb_doses, float):
    #         print(f"Valeur non float : {elt.nb_doses}")

    ODS.objects.bulk_create(ods_objects)
