from rest_framework import serializers
from . import models

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experience
        fields = (
            'id',
            'title',
            'code',
            'created_at',
            'updated_at',
        )


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = (
            'id',
            'title',
            'created_at',
            'updated_at',
        )


class DistrictSerializer(serializers.ModelSerializer):
    region = RegionSerializer(many=True)

    class Meta:
        model = models.District
        fields = (
            'id',   
            'title',
            'region',
            'created_at',
            'updated_at',
        )

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = (
            'id',
            'title',
            'logo',
            'created_at',
            'updated_at',
        )

class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    district = DistrictSerializer()
    experience = ExperienceSerializer()

    class Meta:
        model = models.Vacancy
        fields = (
            'id',
            'title',
            'company',
            'district',
            'experience',
            'price_from',
            'price_to',
            'created_at',
            'updated_at',
        )


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization()
        fields = (
            'id',
            'title',
            'created_at',
            'updated_at',
        )

class SpecializationTypeSerializer(serializers.ModelSerializer):
    specialization = SpecializationSerializer()

    class Meta:
        model = models.SpecializationType()
        fields = (
            'id',
            'title',
            'specialization',
            'created_at',
            'updated_at'
        )