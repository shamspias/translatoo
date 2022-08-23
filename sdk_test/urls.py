from django.urls import path

from .views import ImageView

urlpatterns = [
    path('', ImageView.as_view(), name="image_view"),
]
