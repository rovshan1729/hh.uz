from rest_framework import serializers
from . import models

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experience
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.District
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'

class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    district = DistrictSerializer()
    experience = ExperienceSerializer()

    class Meta:
        model = models.Vacancy
        fields = '__all__'