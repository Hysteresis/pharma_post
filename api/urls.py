from django.urls import path
from api.views import EndPointDose
# app_name = 'api'
urlpatterns = [
    path('', EndPointDose.as_view(), name='endpoint'),
]
