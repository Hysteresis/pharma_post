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

from app.models import D_Type


# Create your tests here.


class MyTestCase(TestCase):

    # def test_get_user(self):
    #     user = User.objects.create_user(username='testUser1', password='12345')
    #     # user.save()
    #     user.is_superuser = True
    #     token = Token.objects.create(user=user)
    #     print(token)
    #     factory = APIRequestFactory()
    #     view = EndPointDose.as_view()
    #     request = factory.get('/api/')
    #     force_authenticate(request, user=user)
    #     response = view(request)
    #     print(f"Methode 1 ===> response sur API/ : {response}")
    #     self.assertEqual(response.status_code, 200)

    def test_get_type_detail(self):
        # user = User.objects.create_user(username='testUser2', password='12345')
        # print(user)
        # user.is_superuser = True
        # token = Token.objects.create(user=user)
        # print(token.key)

        table = 'type'
        pk = "Moderna"
        factory = APIRequestFactory()
        my_dict = {'get': 'retrieve'}
        view = Dose_detail.as_view(actions=my_dict)

        # request = factory.get(reverse("dose_detail"), {'table': table})
        request = factory.get(reverse("dose_detail"), {'table': table})
        print(request)
        # force_authenticate(request, user=user)

        type_response = view(request)
        print(type_response)


        self.assertEqual(type_response.status_code, 200)