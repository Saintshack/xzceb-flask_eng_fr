from deep_translator import MyMemoryTranslator
import requests

def englishToFrench(englishtext):
    url_get = "https://api.mymemory.translated.net/get"
    par = {'q': (englishtext), "langpair":"en|fr"}
    data = requests.get(url_get,params=par)
    french_text = data.json()['responseData']['translatedText']

    return(french_text)




def frenchToEnglish(frenchtext):
    url_get = "https://api.mymemory.translated.net/get"
    par = {'q': (frenchtext), "langpair":"fr|en"}
    data = requests.get(url_get,params=par)
    english_text = data.json()['responseData']['translatedText']

    return(english_text)
















MyMemoryTranslator




