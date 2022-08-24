from django.contrib import admin
from .models import LanguageCode, TranslatedFile

# Register your models here.

admin.site.register(LanguageCode)
admin.site.register(TranslatedFile)
