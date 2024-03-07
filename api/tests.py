from django.test import TestCase
import os
from datetime import date

from django.test import TestCase

from rest_framework.test import APIRequestFactory
from api.views import EndPointDose
import json
# Create your tests here.

# factory = APIRequestFactory()
# request = factory.get('')
# view = EndPointDose.as_view()
# response.render()
# json_response = json.loads(response.content)

class MyTestCase(TestCase):
    def test_my_view(self):
        factory = APIRequestFactory()
        request = factory.get('api/')
        view = EndPointDose.as_view()
        response = view(request)
        response.render()
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, 200)


# from app.models import F_Club, D_Federation, D_Date, D_Sexe, D_Geographie, D_Age, D_Type, ODS, City
# from rugby_new import settings
# from scripts.ETL_ODS import run
#
# # Create your tests here.
#
# factory = APIRequestFactory()
# request = factory.get('cities/75001/')
# view = City_api.as_view()
# response = view(request, postal_code='75001')
# response.render()
# json_response = json.loads(response.content)
#
# # factory = APIRequestFactory()
# # request = factory.delete('formation/63000/')
# # view = API_Formation.as_view()
# class TestClubApi(TestCase):
#     def setUp(self):
#         date_instance = D_Date.objects.create(pk_date="2021-01-01")
#         geographie_instance = D_Geographie.objects.create(
#             pk_geographie="74315-CSZ - Yvoire - nan - 74 - - Auvergne-Rhône-Alpes - 1.Champ geoc",
#             commune="Yvoire", qpv="...", departement="74",
#             nom_departement="Auvergne-Rhône-Alpes", region="...",
#             status_geo="...")
#         federation_instance = D_Federation.objects.create(pk_federation="12345",
#                                                           federation="FF de Sauvetage et de Secourisme")
#         type_instance = D_Type.objects.create(pk_type="EPA")
#         code_instance = f"{date_instance.pk_date}_{geographie_instance.pk_geographie}_{type_instance.pk_type}"
#
#         self.club_instance = F_Club.objects.create(
#             code=code_instance,
#             fk_date=date_instance,
#             fk_geographie=geographie_instance,
#             fk_federation=federation_instance,
#             fk_type=type_instance,
#             nombre=10
#         )
#
#     def test_get_all_clubs(self):
#         request = factory.get('/clubs/')
#         response = view(request)
#         self.assertEqual(response.status_code, 200)
#
#     # def test_error_server(self):
#     #     request = factory.get('/api/clubss/')
#     #     response = view(request)
#     #     print(f"response : {response}")
#         # self.assertEqual(response.status_code, 500)