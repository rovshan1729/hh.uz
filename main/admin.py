from django.contrib import admin
from django.apps import apps

for model in apps.get_models():
    if not admin.site.is_registered(model):
        admin.site.register(model)