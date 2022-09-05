from django.urls import path

from .views import (
    ProofreadingView,
    ProofreadingOpenAIView
)

urlpatterns = [
    path('', ProofreadingView.as_view(), name="proofreading"),
    path('ai', ProofreadingOpenAIView.as_view(), name="proofreading-ai"),
]
