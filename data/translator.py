import os
import time
from colorama import Fore,Back,Style
from matplotlib.pyplot import xkcd
from rich.progress import track
import requests
import re
from bs4 import BeautifulSoup
import csv
import logging
from translate import Translator

def info():
    print(Fore.MAGENTA+
    """
    AFRIKAANS   : af
    ALBANIAN    : sq
    AMHARIC     : am
    ARABIC      : ar
    AZERBAIJANI : az
    BENGALI     : bn
    BOSNIAN     : bs
    BULGARIAN   : bg
    CHINESE (SIMPLIFIED):zh
    CHINESE (TRADITIONAL):zh-TW
    CROATIAN    : hr
    CZECH       : cs
    DANISH      : da
    DARI        : fa-AF
    DUTCH       : nl
    ENGLISH     : en
    ESTONIAN    : et
    FINNISH     : fi
    FRENCH      : fr
    FRENCH (CANADA):fr-CA
    GEORGIAN    : ka
    GERMAN      : de
    GREEK       : el
    HAUSA       : ha
    HEBREW      : he
    HINDI       : hi
    HUNGARIAN   : hu
    INDONESIAN  : id
    ITALIAN     : it
    JAPANESE    : ja
    KOREAN      : ko
    LATVIAN     : lv
    MALAY       : ms
    NORWEGIAN   : no
    PERSIAN     : fa
    PASHTO      : ps
    POLISH      : pl
    PORTUGUESE  : pt
    ROMANIAN    : ro
    RUSSIAN     : ru
    SERBIAN     : sr
    SLOVAK      : sk
    SLOVENIAN   : sl
    SOMALI      : so
    SPANISH     : es
    MEXICO      : es-MX
    SWAHILI     : sw
    SWEDISH     : svz
    TAGALOG     : tl
    TAMIL       : ta
    THAI        : th
    TURKISH     : tr          
    UKRAINIAN   : uk
    URDU        : ur
    VIETNAMESE  : vi
    """)
    

def translate():
    os.system("clear")
    print(Fore.GREEN+"""
            
            -_________________-_________________-
            |                                   |
            |  |-_-| Welcome to E0 Bot!  |-_-|  | 
            -_________________-_________________- 
                
    """)
    lang = input(Fore.MAGENTA+"[+] Which language do you want to translate (for info wire info) : ")
    if lang=="info":
        info()
    translator= Translator(to_lang=lang)
    text = input(Fore.MAGENTA+"[+] Please enter a text to translate: ")
    translation = translator.translate(text)
    print(translation)
    time.sleep(30)

if __name__ == "__main__":
    translate()
