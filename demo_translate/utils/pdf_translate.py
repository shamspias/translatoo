from pdf2docx import parse
from docx2pdf import convert
import os
from django.conf import settings
from .translate_core import language_translation
from pathlib import Path


def translate_pdf(pdf_file, source_ln, target_ln):
    """
    make pdf into word
    translate the word make it into pdf and remove the converted word
    """
    # FILES_DIR = Path(__file__).resolve()
    # file_path = os.path.join(FILES_DIR, pdf_file.my_file.url)
    print(pdf_file.my_file.url)
    pdf_file_name = pdf_file.name
    word_file = target_ln + "_" + pdf_file_name[:-4] + ".docx"
    parse(pdf_file.my_file.path, word_file, start=0, end=None)

    target_word_file = pdf_file_name[:-4] + ".docx"

    language_translation(word_file, target_word_file, source_ln, target_ln)

    new_pdf_file_name = "media/files/" + target_ln + "_" + pdf_file_name
    return_pdf_path = target_ln + "_" + pdf_file_name
    convert(target_word_file, new_pdf_file_name)

    os.remove(word_file)
    os.remove(target_word_file)
    file = "files/" + return_pdf_path
    return file
