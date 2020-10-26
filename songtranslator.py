# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:53:47 2020

@author: RICHA
"""

from googletrans import Translator, LANGUAGES

song='''
Always take a big bite
It’s such a gorgeous sight
To see you eat in the middle of the night
'''
mylang=['it','fr','hi','es','ta']

for lang in mylang:
    t=Translator().translate(song,dest=lang)
    print(lang + '-'+ LANGUAGES[lang])
    print(t.text)
    #song=t.text
    print()