from . import serializers
from . import  views
from . import models
from django.db.models import Count
from rest_framework import generics


class MainPageAPIView(generics.ListAPIView):
    queryset = models.MainPage.objects.all().annotate(
        total_vacancies=Count('vacancy'),
        total_companies=Count('companies'),
    )
    serializer_class = serializers.MainPageSerializer
    filterset_fields = ('total_resumes', 'total_vacancies', 'total_companies')
    search_fields = ('total_resumes', 'total_vacancies', 'total_companies',)


class AnotherCountryAPIView(generics.ListAPIView):
    queryset = models.AnotherCountry.objects.all().select_related('vacancy')
    serializer_class = serializers.AnotherCountrySerializer
    filterset_fields = ('id', 'title', 'vacancy__title',)
    search_fields = ('title', 'vacancy__title')


class WorkByProfessionAPIView(generics.ListAPIView):
    queryset = models.WorkByProfession.objects.all()
    serializer_class = serializers.AnotherCountrySerializer
    filterset_fields = ('id', 'title',)
    search_fields = ('title')


class ArticleAPIView(generics.ListAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    filterset_fields = ('title',)
    search_fields = ('title')


class NewsAPIView(generics.ListAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    filterset_fields = ('title',)
    search_fields = ('title')


class VacancyOfTheDayAPIView(generics.ListAPIView):
    queryset = models.VacancyOfTheDay.objects.select_related(
        'another_countries'
    ).all()
    serializer_class = serializers.VacancyOfTheDaySerializer
    filterset_fields = ('another_countries__title',)
    search_fields = ('another_countries__title')


class JobOfferInAPIView(generics.ListAPIView):
    queryset = models.JobOfferIn.objects.select_related('vacancy').all()
    serializer_class = serializers.JobOfferInSerializer
    filterset_fields = ('vacancy__title',)
    search_fields = ('vacancy__title')


class ProfessionAPIView(generics.ListAPIView):
    queryset = models.Profession.objects.select_related(
        'vacancy'
    ).all().annotate(total_vacancies=Count('vacancy'))
    serializer_class = serializers.ProfessionSerializer
    filterset_fields = ('vacancy__title',)
    search_fields = ('vacancy__title')

    


    
   


