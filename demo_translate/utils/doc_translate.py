import os

from translate_core import language_translation


def translate_docx(doc_file_name, source_ln, target_ln):
    """
    make pdf into word
    translate the word make it into pdf and remove the converted word
    """
    doc_file_name = doc_file_name + "x"
    word_file = target_ln + "_" + doc_file_name

    language_translation(doc_file_name, word_file, source_ln, target_ln)

    os.remove(word_file)
    return True
