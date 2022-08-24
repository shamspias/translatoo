from django import forms

from .models import LanguageCode, TranslatedFile

LANGUAGES = (
    ('af', 'Afrikaans'),
    ('ar', 'Arabic'),
    ('be', 'Belarusian'),
    ('bn', 'Bengali'),
    ('da', 'Danish'),
    ('nl', 'Dutch'),
    ('en', 'English'),
    ('ja', 'Japanese'),
    ('tr', 'Turkish'),
    ('uk', 'Ukrainian'),
    ('ur', 'Urdu'),
    ('uz', 'Uzbek'),
    ('he', 'Hebrew')
)


class LanguageModelForm(forms.ModelForm):
    """
    Show all language code in template
    """

    destination = forms.CharField(widget=forms.Select(choices=LANGUAGES, attrs={"type": "text",
                                                                                "class": "form-control",
                                                                                "name": "destination_language",
                                                                                "id": "destination_language", }))

    class Meta:
        model = LanguageCode
        fields = ('short_code', 'destination')
        widgets = {
            'short_code': forms.Select(
                choices=LANGUAGES,
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "source_language",

                }),
            'destination': forms.Select(
                choices=LANGUAGES,
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "destination_language",

                }),
        }


class FileModelForm(forms.ModelForm):
    """
    File filed to download
    """

    class Meta:
        model = TranslatedFile
        fields = ("my_file",)
        widgets = {
            'my_file': forms.FileInput(
                attrs={
                    "type": "file",
                    "class": "form-control form-control-lg",
                    "name": "my_file",
                    "id": "formFileLg",

                }),

        }
