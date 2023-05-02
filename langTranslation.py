from googletrans import Translator

from lang import Language

tl = Translator()


# Part of Code Which helps in Google Translation
def translateLang(targetLang, inputText):
    t_lang = Language.langKey(targetLang)
    result = tl.translate(inputText, dest=t_lang)
    inp_dect = Language.lang(result.src)
    out_dect = Language.lang(result.dest)
    return f"Translated text : {result.text}\nPronunciation : {result.pronunciation}\nInput language detected : {inp_dect}\nOutput language : {out_dect}"

def translateLangDefault(inputText):
    result = tl.translate(inputText, dest="hi")
    inp_dect = Language.lang(result.src)
    out_dect = Language.lang(result.dest)
    return f"Translated text : {result.text}\nPronunciation : {result.pronunciation}\nInput language detected : {inp_dect}\nOutput language : {out_dect}"

def keyword_req(message):
    request = message.text.split()
    keyword = request[0]
    if len(request)<2 or keyword.lower() not in "tl":
        return False
    else:
        return True