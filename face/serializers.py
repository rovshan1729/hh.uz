from rest_framework import serializers
from . import models
from main.serializers import VacancySerializer

class AnotherCountrySerializer(serializers.ModelSerializer):
    vacancy = VacancySerializer()

    class Meta:
        model = models.AnotherCountry
        fields = (
            'id',
            'title',
            'vacancy',
            'created_at',
            'updated_at',
        )

class WorkByProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkByProfession
        fiels = (
            'id',
            'title',
            'created_at',
            'updated_at',
        )

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = (
            'id',
            'title',
            'image',
            'created_at',
            'updated_at',
        )

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = (
            'id',
            'title',
            'image',
            'created_at',
            'updated_at',
        )

class VacancyOfTheDaySerializer(serializers.ModelSerializer):
    another_countries = AnotherCountrySerializer()

    class Meta:
        model = models.VacancyOfTheDay
        fields = (
            'id',
            'another_countries',
            'created_at',
            'updated_at',
        )

class JobOfferInSerializer(serializers.ModelSerializer):
    vacancy = VacancySerializer()

    class Meta:
        model = models.JobOfferIn
        fields = (
            'id',
            'vacancy',
            'created_at',
            'updated_at',
        )


class ProfessionSerializer(serializers.ModelSerializer):
    vacancy = VacancySerializer()

    class Meta:
        model = models.Profession
        fields = (
            'id',
            'vacancy',
            'created_at',
            'updated_at',
        )


class MainPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MainPage
        fields = (
            'id',
            'total_resumes',
            'vacancy',
            'companies',
            'created_at',
            'updated_at',
        )