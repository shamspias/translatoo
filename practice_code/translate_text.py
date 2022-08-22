from googletrans import Translator, constants
from pprint import pprint

# init the Google API translator
translator = Translator()

string = input()

# translate text by given src to destination
translation = translator.translate(string, src="bn", dest="en")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
