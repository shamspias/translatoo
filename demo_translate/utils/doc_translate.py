import os

from .translate_core import language_translation


def translate_doc(doc_file_name, source_ln, target_ln):
    """
    translate the word
    """
    doc_file_name = doc_file_name + "x"
    word_file = target_ln + "_" + doc_file_name
    new_doc_file_name = "media/files/" + word_file
    language_translation(doc_file_name, new_doc_file_name, source_ln, target_ln)

    return "files/" + word_file
