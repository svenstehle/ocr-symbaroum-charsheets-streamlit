# License: APACHE LICENSE, VERSION 2.0

from textblob import TextBlob


def translate_text_to(text, to):
    # translate the text into a different language
    tb = TextBlob(text)
    translated = tb.translate(to=to)
    # show the translated text
    print("TRANSLATED")
    print("==========")
    print(translated)
    return translated
