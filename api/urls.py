from django.urls import path
from api.views import EndPointDose, Dose_detail

# app_name = 'api'
urlpatterns = [
    path('', EndPointDose.as_view(), name='endpoint'),
    path('detail/', Dose_detail.as_view(), name='dose_detail'),
]
