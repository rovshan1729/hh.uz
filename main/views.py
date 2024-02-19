from . import models
from .serializers import *
from rest_framework import generics


class VacancyAPIView(generics.ListAPIView):
    queryset = models.Vacancy.objects.all()
    serializer_class = VacancySerializer
