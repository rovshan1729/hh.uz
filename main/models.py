from django.db import models
from utils.models import BaseModel


class Company(BaseModel):
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title
    
class Region(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class District(BaseModel):
    title = models.CharField(max_length=255)
    region = models.ManyToManyField(Region)

    def __str__(self):
        return self.title
    
class Specialization(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class SpecializationType(BaseModel):
    title = models.CharField(max_length=255)
    specialization = models.ForeignKey(
        Specialization, on_delete=models.CASCADE, related_name='specialization_type'
    )
    
    def __str__(self):
        return self.title
    
    
class Experience(BaseModel):
    title = models.CharField(unique=True, max_length=255)
    code = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class Vacancy(BaseModel):
    title = models.CharField(max_length=255)

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)

    price_from = models.IntegerField(blank=True, null=True)
    price_to = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class PartTimeJob(BaseModel):
    title = models.CharField(max_length=255)
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name='part_time_job'
    )
    counter = models.IntegerField(default=0, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class CompanyIndustry(BaseModel):
    title = models.CharField(max_length=255)
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name='company_industry'
    )
    counter = models.IntegerField(default=0, blank=True, null=True)
    
    def __str__(self):
        return self.title

class Education(BaseModel):
    title = models.CharField(max_length=255)
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name='education'
    )
    
    counter = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.title
 
class OtherOption(BaseModel):
    title = models.CharField(max_length=255)
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name='other_option'
    )
    
    counter = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.title

class KeyWords(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Schedule(BaseModel):
    title = models.CharField(max_length=255)
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, related_name='schedule'
    )
    
    counter = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.title
    
