from django.db import models


# Create your models here.

class LanguageCode(models.Model):
    """
    name of language code
    """
    short_code = models.CharField(max_length=10, blank=True, null=True)
    language_name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.language_name


class TranslatedFile(models.Model):
    """
    File to translate
    """
    name = models.CharField(max_length=200, blank=True, null=True)
    my_file = models.FileField(upload_to='files/', blank=True, null=True)
    translated_file = models.FileField(upload_to='translated/', blank=True, null=True)

    def __str__(self):
        return "File : "

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
