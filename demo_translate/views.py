from django.shortcuts import render
from django.views.generic import TemplateView

from .models import LanguageCode, TranslatedFile
from .forms import LanguageModelForm, FileModelForm
from .utils import (
    translate_docx,
    translate_doc,
    translate_pdf,
)


def check_pdf(filename):
    print('file name', filename)
    if filename.endswith('.pdf'):
        return True
    else:
        return False


def check_doc(filename):
    print('file name', filename)
    if filename.endswith('.doc'):
        return True
    else:
        return False


def check_docx(filename):
    print('file name', filename)
    if filename.endswith('.docx'):
        return True
    else:
        return False


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
        my_file = request.FILES.get('my_file')
        source_language = request.POST.get('short_code')
        destination_language = request.POST.get('destination')

        if my_file:
            _file = TranslatedFile.objects.create(name=my_file.name, my_file=my_file)
            file_obj = TranslatedFile.objects.get(name__exact=my_file.name)
            if check_pdf(file_obj.name):
                translate_pdf(file_obj.my_file, source_language, destination_language)

            # try:
            #     file_obj = TranslatedFile.objects.create(name=my_file.name, my_file=my_file)
            #
            #     if file_obj.my_file.check_pdf(my_file.name):
            #         translate_pdf(my_file, source_language, destination_language)
            #     elif file_obj.my_file.check_doc(my_file.name):
            #         translate_doc(my_file, source_language, destination_language)
            #     elif file_obj.my_file.check_docx(my_file.name):
            #         translate_docx(my_file, source_language, destination_language)
            # except Exception:
            #     print("Error Upload")

        context = {
            "language_form": self.language_code,
            "file_form": self.file_filed,
        }
        return render(request, 'translate_files.html', context=context)
