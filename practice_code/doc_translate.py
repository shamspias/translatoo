import pypandoc
from bs4 import BeautifulSoup
import re

from deep_translator import (GoogleTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator,
                             DeeplTranslator,
                             QcriTranslator,
                             single_detection,
                             batch_detection)


def translate_language(source, ext):
    document_name = source + "." + ext
    output = pypandoc.convert_file(document_name, 'html5')
    soup = BeautifulSoup(output, features="lxml")
    print("-----------------------")
    target_tags = re.findall(r'<.+?>', output)  # get all html tags
    target_tags = list(dict.fromkeys(target_tags))  # removing duplicates
    for i, word in enumerate(target_tags):
        target_tags[i] = word.replace('</', '<')
        target_tags[i] = target_tags[i].replace('<', '')
        target_tags[i] = target_tags[i].replace('>', '')

        if " " in target_tags[i]:
            target_tags[i] = target_tags[i][:target_tags[i].index(" ")]

    target_tags = list(dict.fromkeys(target_tags))  # removing duplicates

    for i in soup.findAll(target_tags):
        try:
            i.string.replace_with(GoogleTranslator(source='auto', target='german').translate(i.string))
        except:
            print("error")
    print(soup)


print("Please enter source document name.")
source = input().strip()
translate_language(source, "docx")
