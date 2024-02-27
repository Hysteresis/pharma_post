from django.urls import path
from api.views import EndPointClub
# app_name = 'api'
urlpatterns = [
    path('', EndPointClub.as_view(), name='endpoint'),
]