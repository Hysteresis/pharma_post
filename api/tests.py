from django.test import TestCase
import os
from datetime import date

from django.test import TestCase

from rest_framework.test import APIRequestFactory, force_authenticate
from api.views import EndPointDose
from django.contrib.auth.models import User, Permission
import json


# Create your tests here.


class MyTestCase(TestCase):

    def test_get_user(self):
        user = User.objects.create_user(username='testuser', password='12345')
        user.is_superuser = True
        user.save()
        factory = APIRequestFactory()
        view = EndPointDose.as_view()
        request = factory.get('api/')
        force_authenticate(request, user=user)
        response = view(request)

        self.assertEqual(response.status_code, 200)

    def test_get_data(self):
        expected_count = 33212
        data = {
            "count": expected_count
        }
        self.assertIn("count", data)
        self.assertEqual(data["count"], expected_count)



