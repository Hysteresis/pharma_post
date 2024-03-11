from django.db.models import Sum
from django.shortcuts import render
from django.contrib.sites import requests
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.permissions import IsAdminUser

from app.models import F_Dose, D_Date, D_Type, D_Geographie
from pharma_post.serializers import FDoseSerializer, DDateSerializer, DTypeSerializer, DGeographieSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class IsSuperAdmin(IsAdminUser):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class EndPointDose(APIView):
    permission_classes = [IsSuperAdmin]
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 4
        doses = F_Dose.objects.all().order_by('fk_date')
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

    def get_serializer(self):
        """
        defini le serializer en fonction du parametre d'URL ?table=

        """
        table = self.request.query_params.get('table', None)

        if table == 'date':
            return DDateSerializer
        elif table == 'type':
            return DTypeSerializer
        elif table == 'geographie':
            return DGeographieSerializer
        elif table == 'dose':
            return FDoseSerializer
        else:
            return None

    def get_queryset(self, table, pk):
        """
        defini la table en fonction du paramètre 'table' et filtre sur la 'pk'
        """
        if table == 'date':
            return D_Date.objects.filter(date=pk)
        elif table == 'type':
            return D_Type.objects.filter(pk=pk)
        elif table == 'geographie':
            return D_Geographie.objects.filter(pk=pk)
        elif table == 'dose':
            return F_Dose.objects.filter(pk=pk)
        else:
            return None


class Dose_detail(APIView):
    # http://127.0.0.1:8000/api/detail/?table=dose&pk=2022-11-13-Pfizer-976-6
    # http://127.0.0.1:8000/api/detail/?table=dose
    permission_classes = [IsSuperAdmin]
    # def get(self, request, format=None):
    def get(self, request):
        """
        prend en paramèetre d'url 'table' OU 'table' et 'pk'

        """
        table = self.request.query_params.get('table', None)
        pk = self.request.query_params.get('pk', None)

        if not table:
            return Response({'message': 'Paramètre "table" manquant'}, status=status.HTTP_400_BAD_REQUEST)

        if pk is None:
            queryset = self.get_queryset(table)
            serializer_class = self.get_serializer(table)
        else:
            queryset = self.get_queryset(table, pk)
            serializer_class = self.get_serializer(table)

        if not queryset or not serializer_class:
            return Response({'message': 'Table ou clé primaire invalide'}, status=status.HTTP_400_BAD_REQUEST)

        nombre_de_lignes = queryset.count()
        paginator = PageNumberPagination()
        paginator.page_size = 25
        paginated_queryset = paginator.paginate_queryset(queryset, request)

        serializer = serializer_class(paginated_queryset, many=True)
        # serializer = serializer_class(queryset, many=True)
        result = {
            'home': 'http://localhost:8000/admin',
            'nombre_de_lignes': nombre_de_lignes,
            'nom_de_table': table,
            'status OK': status.HTTP_200_OK,
            'data': serializer.data,

            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link()
        }
        print("ok = 200")
        return Response(result, status=status.HTTP_200_OK)

    def get_serializer(self, table=None):
        """
        prend en parametre d'URL la 'table'

        """
        if table is None:
            table = self.request.query_params.get('table', None)

        if table == 'date':
            return DDateSerializer
        elif table == 'type':
            return DTypeSerializer
        elif table == 'geographie':
            return DGeographieSerializer
        elif table == 'dose':
            return FDoseSerializer
        else:
            return None

    def get_queryset(self, table, pk=None):
        """
        prend en paramètre 'table
        """
        if table == 'date':
            if pk is not None:
                return D_Date.objects.filter(pk=pk).order_by('pk_date')
            else:
                return D_Date.objects.all().order_by('pk_date')
        elif table == 'type':
            if pk is not None:
                return D_Type.objects.filter(pk=pk).order_by('pk_type')
            else:
                return D_Type.objects.all()
        elif table == 'geographie':
            if pk is not None:
                return D_Geographie.objects.filter(pk=pk).order_by('pk_geographie')
            else:
                return D_Geographie.objects.all()
        elif table == 'dose':
            if pk is not None:
                return F_Dose.objects.filter(pk=pk).order_by('pk_dose')
            else:
                return F_Dose.objects.all()
        else:
            return None
