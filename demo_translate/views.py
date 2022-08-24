from django.shortcuts import render
from django.views.generic import TemplateView

from .models import LanguageCode
from .forms import LanguageModelForm, FileModelForm
from .utils import (
    translate_docx,
    translate_doc,
    translate_pdf,
)


class DocumentTranslateView(TemplateView):
    """
    Test Translate files
    """
    template_name = "translate_files.html"
    language_code = LanguageModelForm()
    file_filed = FileModelForm()

    def get(self, request, *args, **kwargs):
        context = {
            "language_form": self.language_code,
            "file_form": self.file_filed,
        }
        return render(request, 'translate_files.html', context=context)

    def post(self, request, *args, **kwargs):
        my_file = request.POST.get('my_file')
        source_language = request.POST.get('source_language')
        destination_language = request.POST.get('destination_language')
        print(my_file)
        print(source_language)
        print(destination_language)
        if my_file is not None:
            if self.check_pdf(my_file):
                translate_pdf(my_file, source_language, destination_language)

            elif self.check_doc(my_file):
                translate_doc(my_file, source_language, destination_language)

            elif self.check_docx(my_file):
                translate_docx(my_file, source_language, destination_language)
        context = {
            "language_form": self.language_code,
            "file_form": self.file_filed,
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
