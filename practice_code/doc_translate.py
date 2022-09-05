import pypandoc
import re
from googletrans import Translator
import requests


def translate_language(source, ext):
    document_name = source + "." + ext
    output = pypandoc.convert_file(document_name, 'html5')
    my_string = re.findall(r'>(.+?)<', output)
    print(my_string)
    # translator = Translator()
    for i, para in enumerate(my_string):
        data = {
            "source": "auto",
            "target": "de",
            "text": para,
            "proxies": [],
        }
        response = requests.post('https://deep-translator-api.azurewebsites.net/google/', json=data)
        if response.json()["translation"] is None:
            continue
        my_string[i] = response.json()["translation"]
    # for i, para in enumerate(my_string):
    #     try:
    #         translation = translator.translate(para, dest="bn")
    #         my_string[i] = translation.text
    #     except:
    #         print("Error " + str(i))
    print(my_string)


print("Please enter source document name.")
source = input().strip()
translate_language(source, "docx")
