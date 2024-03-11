from django.test import TestCase
import os
from datetime import date

from django.test import TestCase

from rest_framework.test import APIRequestFactory, force_authenticate, APIClient
from api.views import EndPointDose, Dose_detail
from django.contrib.auth.models import User, Permission
from rest_framework.authtoken.models import Token
from rest_framework.test import force_authenticate
from django.urls import reverse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

import json

from app.models import D_Type, D_Date, D_Geographie, F_Dose


# Create your tests here.


class MyTestCase(TestCase):
    def setUp(self):
        self.type_moderna = D_Type.objects.create(pk_type="Moderna")
        self.date = D_Date.objects.create(pk_date="2021-06-13")
        self.geographie = D_Geographie.objects.create(pk_geographie="01-84")

        type_moderna = D_Type.objects.get(pk_type="Moderna")
        date = D_Date.objects.get(pk_date="2021-06-13")
        geographie = D_Geographie.objects.get(pk_geographie="01-84")

        self.dose = F_Dose.objects.create(pk_dose="2021-06-13-AstraZeneca-01-84", nb_ucd=1.0, nb_doses=1.0,
                                          fk_date=date, fk_type=type_moderna, fk_geographie=geographie)

        user = User.objects.create_user(username='testUser3', password='12345')
        user.is_superuser = True
        token = Token.objects.create(user=user)

    def test_get_user(self):
        factory = APIRequestFactory()
        view = EndPointDose.as_view()
        request = factory.get('/api/')
        force_authenticate(request, user=User)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_get_type_moderna(self):
        table = 'type'
        pk = "Moderna"
        factory = APIRequestFactory()
        view = Dose_detail.as_view()
        url = reverse("dose_detail") + f'?table={table}&pk={pk}'
        request = factory.get(url)
        force_authenticate(request, user=User)
        response = view(request)

        self.assertEqual(response.status_code, 200)

    def test_get_date_detail(self):

        table = 'date'
        pk = "2021-06-13"
        factory = APIRequestFactory()
        view = Dose_detail.as_view()
        url = reverse("dose_detail") + f'?table={table}&pk={pk}'
        request = factory.get(url)
        force_authenticate(request, user=User)
        response = view(request)

        self.assertEqual(response.status_code, 200)

    def test_get_geographie_detail(self):

        table = 'geographie'
        pk = "01-84"
        factory = APIRequestFactory()
        view = Dose_detail.as_view()
        url = reverse("dose_detail") + f'?table={table}&pk={pk}'
        request = factory.get(url)
        force_authenticate(request, user=User)
        response = view(request)

        self.assertEqual(response.status_code, 200)


    def test_get_dose_detail(self):
        table = 'dose'
        pk = "2021-06-13-AstraZeneca-01-84"
        factory = APIRequestFactory()
        view = Dose_detail.as_view()
        url = reverse("dose_detail") + f'?table={table}&pk={pk}'
        request = factory.get(url)
        force_authenticate(request, user=User)
        response = view(request)
        print("test 5")
        print(request)
        print(response)

        self.assertEqual(response.status_code, 200)
