from django.urls import path

from .views import (
    GenerateBlogTopicsView,
    GenerateBlogSectionsView,
    BlogSectionExpanderView,

)

urlpatterns = [
    path('topic/', GenerateBlogTopicsView.as_view(), name="blog-topics"),
    path('sections/', GenerateBlogSectionsView.as_view(), name="blog-sections"),
    path('sections/expander/', BlogSectionExpanderView.as_view(), name="blog-sections-expander"),
]
