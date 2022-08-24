from django.shortcuts import render
from django.views.generic import TemplateView
import random
import string

from .models import LanguageCode, TranslatedFile
from .forms import LanguageModelForm, FileModelForm
from .utils import (
    translate_docx,
    translate_doc,
    translate_pdf,
)


def check_pdf(filename):
    if filename.endswith('.pdf'):
        return True
    else:
        return False


def check_doc(filename):
    if filename.endswith('.doc'):
        return True
    else:
        return False


def check_docx(filename):
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
            random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
            new_name = random_name + my_file.name
            _file = TranslatedFile.objects.create(name=new_name, my_file=my_file)
            file_obj = TranslatedFile.objects.get(name__exact=new_name)
            if check_pdf(file_obj.name):
                translated_file = translate_pdf(file_obj, source_language, destination_language)
                file_obj.translated_file = translated_file
                file_obj.save()
            elif check_docx(file_obj.name):
                translated_file = translate_docx(file_obj, source_language, destination_language)
                file_obj.translated_file = translated_file
                file_obj.save()
            elif check_doc(file_obj.name):
                translated_file = translate_doc(file_obj, source_language, destination_language)
                file_obj.translated_file = translated_file
                file_obj.save()
            # _file.delete()

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
