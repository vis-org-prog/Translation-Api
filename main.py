import os 
import pprint

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service-account.json"

def translate_text(target: str, text: str) -> dict:
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print("Text: {}".format(result["input"]))
    print("Translation: {}".format(result["translatedText"]))
    print("Detected source language: {}".format(result["detectedSourceLanguage"]))

    return result

text_to_translate = "hello world"

# List of target languages
target_languages = ["fr", "es", "de", "it", "ja", "zh"]

# Loop through each target language and translate the text
for lang in target_languages:
    print(f"\nTranslating 'hello world' to {lang}:\n")
    translate_text(lang, text_to_translate)
