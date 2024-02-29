from django.db.models import Sum
from django.shortcuts import render
from django.contrib.sites import requests
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.models import F_Dose
from pharma_post.serializers import FDoseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class EndPointDose(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 4

        doses = F_Dose.objects.all()
        data_F_Dose_page = paginator.paginate_queryset(doses, request)
        data_F_Dose_serializer = FDoseSerializer(data_F_Dose_page, many=True)
        total_doses = F_Dose.objects.aggregate(total_doses=Sum('nb_doses'))['total_doses']


        data = {
            'num_doses': doses.count(),
            'total_doses': total_doses,
            'data_F_Dose': data_F_Dose_serializer.data,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
        }

        return paginator.get_paginated_response(data)
