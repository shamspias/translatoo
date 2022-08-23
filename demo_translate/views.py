from django.shortcuts import render
from django.views.generic import TemplateView
from .utils import (
    translate_docx,
    translate_doc,
    translate_pdf,
)
from six import BytesIO


class DocumentTranslateView(TemplateView):
    """
    Test Translate files
    """
    template_name = "translate_files.html"

    def get(self, request, *args, **kwargs):
        my_file = request.GET.get('my_file')
        source_language = request.GET.get('source_language')
        destination_language = request.GET.get('destination_language')

        if my_file is not None:
            if self.check_pdf(my_file):
                translate_pdf(my_file, source_language, destination_language)

            elif self.check_doc(my_file):
                translate_doc(my_file, source_language, destination_language)

            elif self.check_docx(my_file):
                translate_docx(my_file, source_language, destination_language)

        context = {
            "file": my_file
        }
        return render(request, 'translate_files.html', context=context)

    def post(self, request, *args, **kwargs):
        my_file = request.GET.get('my_file')
        context = {
            "file": my_file
        }
        return render(request, 'translate_files.html', context=context)

    def check_pdf(self, filename):
        print('file name', filename)
        if filename.endswith('.pdf'):
            return True
        else:
            return False

    def check_doc(self, filename):
        print('file name', filename)
        if filename.endswith('.doc'):
            return True
        else:
            return False

    def check_docx(self, filename):
        print('file name', filename)
        if filename.endswith('.docx'):
            return True
        else:
            return False
