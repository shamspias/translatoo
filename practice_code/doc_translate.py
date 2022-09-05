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
    my_string = re.findall(r'>(.+?)<', output)
    my_string_old = my_string.copy()
    print(my_string)
    # translator = Translator()
    for i, para in enumerate(my_string):
        try:
            translated = GoogleTranslator(source='auto', target='german').translate(para)
            my_string[i] = translated
        except:
            print("Error")
    print("-----------------------")
    print(my_string)
    print("-----------------------")
    soup = BeautifulSoup(output, features="lxml")
    print("-----------------------")
    target = soup.find_all(text=r'>(.+?)<')
    print(target)
    print("-----------------------")
    for v in target:
        v.replace_with(v.replace(my_string_old[v], my_string[v]))
    print(soup)


print("Please enter source document name.")
source = input().strip()
translate_language(source, "docx")
