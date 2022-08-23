from django.shortcuts import render
from django.views.generic import TemplateView


class DocumentTranslateView(TemplateView):
    """
    Test Translate files
    """
    template_name = "translate_files.html"

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass
