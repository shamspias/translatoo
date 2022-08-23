from googletrans import Translator, constants
from pprint import pprint

# init the Google API translator
translator = Translator()


def translate_string(my_string, language="en", target="de"):
    # translate text by given src to destination
    translation = translator.translate(my_string, src=language, dest=target)
    # print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    return translation.text
#
#
# class TestTranslate:
#     string = input("Enter your text: ")
#     sentences = [
#         "Hello everyone",
#         "How are you ?",
#         "Do you speak english ?",
#         "Good bye!"
#     ]
#
#     # translate list of text by given src to destination
#     for i in sentences:
#         translation = translator.translate(i, src="en", dest="bn")
#         print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
#
#
# if __name__ == '__main__':
#     pass
