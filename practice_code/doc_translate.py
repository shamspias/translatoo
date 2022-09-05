import pypandoc
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


print("Please enter source document name.")
source = input().strip()
translate_language(source, "docx")
