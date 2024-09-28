
import goslate
import googletrans
from googletrans import Translator

# Translator by goslate
'''
text=input('enter text: ')
gs=goslate.Goslate()
languages=gs.get_languages()
lang_detect=gs.detect(text)
print(languages[lang_detect])
for key, value in languages.items():
    print(f'{key} {value}')
while True:   
    choice=(input('choose translation langugage:'))
    if choice in languages.keys():
        translated=gs.translate(text,choice)
        print(translated)
    else:
        choice=(input('choose translation langugage:'))
        '''

# Translator by googletrans
translator=Translator()
text=input('enter your text here: ')
print(translator.detect(text))
for i, la, lang in zip(range(len(googletrans.LANGUAGES)), googletrans.LANGUAGES.keys(), googletrans.LANGUAGES.values()):
        i+=1
        print(f"{i}-{la}:{lang}") # all available languages
while True:
    choose_lang=input('enter language to translate text: ') #choose by first 2 letters (googletrans.LANGUAGES.keys())
    if choose_lang in googletrans.LANGUAGES:
        translated=translator.translate(text,dest=choose_lang)
        print(translated.text) # prints the translated text only
    else:
        print('not valid choice')



  
    




    

  