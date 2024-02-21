from django.db import models
from utils.models import BaseModel
from main.models import Vacancy, Company


class AnotherCountry(BaseModel):
    title = models.CharField(max_length=255, unique=True)
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name='vacancy'
    )
    def __str__(self):
        return self.title
    
class WorkByProfession(BaseModel):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title
    
class Article(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title
    
class News(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title
    
class VacancyOfTheDay(BaseModel):

    another_countries = models.ForeignKey(
        AnotherCountry, on_delete=models.CASCADE, related_name='vacancy_of_the_day'
    )
    

class JobOfferIn(BaseModel):
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name='job_offer'
    )

class Profession(BaseModel):
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name='professions'
    )
    
class MainPage(BaseModel):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='main_page')
    companies = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company')
    total_resumes = models.IntegerField(blank=True, null=True)
   

    

