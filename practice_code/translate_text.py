from googletrans import Translator, constants
from pprint import pprint

# init the Google API translator
translator = Translator()

# translate text by given src to destination
translation = translator.translate("কি খবর", src="bn", dest="en")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")