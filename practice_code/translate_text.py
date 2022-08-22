from googletrans import Translator, constants
from pprint import pprint

# init the Google API translator
translator = Translator()

string = input("Enter your text: ")
sentences = [
    "Hello everyone",
    "How are you ?",
    "Do you speak english ?",
    "Good bye!"
]

# translate text by given src to destination
translation = translator.translate(string, src="bn", dest="en")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

# translate list of text by given src to destination
for i in sentences:
    translation = translator.translate(i, src="en", dest="bn")
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")