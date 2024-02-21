from . import models
from .serializers import VacancySerializer, SpecializationTypeSerializer
from rest_framework import generics


class VacancyAPIView(generics.ListAPIView):
    queryset = models.Vacancy.objects.select_related(
        'company', 'district', 'experience', 
    ).all()
    serializer_class = VacancySerializer
    filterset_fields = (
        'id',
        'title',
        'company',
        'district',
        'experience',
        'price_from',
        'price_to',
    )
    search_fields = ('title', 'company__title', 'price_from')     
    
class SpecializationAPIView(generics.ListAPIView):
    queryset = models.SpecializationType.objects.select_related(
        'specialization'
    ).all()
    serializer_class = SpecializationTypeSerializer
    filterset_fields = ('title',)
    search_fields = ('title')


    
