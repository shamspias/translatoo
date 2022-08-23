from django.urls import path

from .views import (
    DocumentTranslateView
)

urlpatterns = [
    path('', DocumentTranslateView.as_view(), name="document_translate_view"),
]
