from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from azure.core.exceptions import HttpResponseError
import os
from dotenv import load_dotenv
load_dotenv()   

TRANSLATE_APIKEY = os.getenv('TRANSLATE_APIKEY')
TRANSLATE_TEXT = os.getenv('TRANSLATE_TEXT')
TRANSLATE_REGION = os.getenv('TRANSLATE_REGION')

def translate_text(text, ppl, lang) -> list[str]:
    credential = TranslatorCredential(TRANSLATE_APIKEY, TRANSLATE_REGION)
    text_translator = TextTranslationClient(endpoint=TRANSLATE_TEXT, credential=credential)
    try:
        source_language = "fr"
        target_languages = [lang]
    
        if ppl:
            if ppl == 1:
                text ="Une personne(s) seulement dans le studio s'il vous plait, " + text
            else:
                text = str(ppl) + " personne(s) seulement dans le studio s'il vous plait, " + text
        else:
            text = "Aucune personne(s) dans le studio s'il vous plait, " + text

        input_text_elements = [ InputTextItem(text= text) ]

        response = text_translator.translate(content = input_text_elements, to = target_languages, from_parameter = source_language)
        translation = response[0] if response else None 
        if translation:
            return translation.translations[0].text , text
    except HttpResponseError as exception: 
        print(f"Error Code: {exception.error.code}")
        print(f"Message: {exception.error.message}")
        
