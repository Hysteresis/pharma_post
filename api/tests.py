from django.test import TestCase
import os
from datetime import date

from django.test import TestCase

from rest_framework.test import APIRequestFactory
from api.views import EndPointDose
import json
# Create your tests here.


class MyTestCase(TestCase):
    def test_my_view(self):
        factory = APIRequestFactory()
        request = factory.get('')
        view = EndPointDose.as_view()
        response = view(request)
        response.render()
        json_response = json.loads(response.content)
        # json_str = json.dumps(json_response)
        # print(json_str[:100])
        self.assertEqual(response.status_code, 200)

    def test_json_response_contains_expected_fields(self):
        factory = APIRequestFactory()
        request = factory.get('api/')
        view = EndPointDose.as_view()
        response = view(request)
        response.render()
        json_response = json.loads(response.content)

        self.assertIn('count', json_response)
        self.assertIn('num_doses', json_response['results'])
        self.assertIn('total_doses', json_response['results'])
        self.assertIn('data_F_Dose', json_response['results'])

    def test_data_F_Dose_contains_items(self):
        factory = APIRequestFactory()
        request = factory.get('api/')
        view = EndPointDose.as_view()
        response = view(request)
        response.render()
        json_response = json.loads(response.content)

        self.assertIn('data_F_Dose', json_response['results'])

        for item in json_response['results']['data_F_Dose']:
            print(f"test : {item['pk_dose']}")
            self.assertIn('pk_dose', item)


