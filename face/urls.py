from . import views
from django.urls import path

urlpatterns = [
    path('main-page/', views.MainPageAPIView.as_view()),

    path('another-country/', views.AnotherCountryAPIView.as_view()),

    path('workby-profession/', views.WorkByProfessionAPIView.as_view()),

    path('article/', views.ArticleAPIView.as_view()),

    path('news/', views.NewsAPIView.as_view()),

    path('vacancy-theday/', views.VacancyOfTheDayAPIView.as_view()),

    path('job-offer/', views.JobOfferInAPIView.as_view()),

    path('profession/', views.ProfessionAPIView.as_view()),
]