from django.shortcuts import render
from django.contrib.sites import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.models import F_Dose
from pharma_post.serializers import FDoseSerializer


# Create your views here.


class EndPointClub(APIView):
    # http://127.0.0.1:8000/api/
    def get(self, request):
        doses = F_Dose.objects.all()
        serializer = FDoseSerializer(doses, many=True)
        data = {
            'num_doses': doses.count(),
            'doses': serializer.data

        }
        return Response(data)
