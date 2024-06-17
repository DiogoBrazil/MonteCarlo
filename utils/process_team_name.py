import unicodedata

def remove_accents_and_insert_underlining(text):
    text = text.lower()
    text = text.replace(" ","-")
    text = unicodedata.normalize('NFD', text)
    text = ''.join([c for c in text if not unicodedata.combining(c)])
    return unicodedata.normalize('NFC', text)