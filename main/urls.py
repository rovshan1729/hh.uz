from .views import VacancyAPIView, SpecializationAPIView
from django.urls import path


urlpatterns = [
    path('vacancy/', VacancyAPIView.as_view()),
    path('specialization/', SpecializationAPIView.as_view()),
]