from .views import VacancyAPIView
from django.urls import path


urlpatterns = [path('vacancy/', VacancyAPIView.as_view())]