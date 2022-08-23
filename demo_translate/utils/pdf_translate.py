from pdf2docx import parse
from docx2pdf import convert
import os

from translate_core import language_translation


def translate_pdf(pdf_file_name, source_ln, target_ln):
    """
    make pdf into word
    translate the word make it into pdf and remove the converted word
    """
    word_file = target_ln + "_" + pdf_file_name[:-3]
    parse(pdf_file_name, word_file, start=0, end=None)
    target_word_file = pdf_file_name[:-3] + ".docx"

    language_translation(word_file, target_word_file, source_ln, target_ln)

    new_pdf_file_name = target_ln + "_" + pdf_file_name
    convert(target_word_file, new_pdf_file_name)

    os.remove(word_file)
    os.remove(target_word_file)
    return True
