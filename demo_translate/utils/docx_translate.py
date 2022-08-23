import os

from .translate_core import language_translation


def translate_docx(doc_file_name, source_ln, target_ln):
    """
    translate the word
    """
    word_file = target_ln + "_" + doc_file_name

    language_translation(doc_file_name, word_file, source_ln, target_ln)

    os.remove(word_file)
    return True
