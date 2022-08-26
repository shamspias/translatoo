from django.urls import path

from .views import (
    ProofreadingView
)

urlpatterns = [
    path('', ProofreadingView.as_view(), name="proofreading"),
]
