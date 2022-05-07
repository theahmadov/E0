import os
import time
from colorama import Fore,Back,Style
from rich.progress import track
import E1 as E0
import requests
import re
from bs4 import BeautifulSoup
import csv
import logging
import cv2 

def loading(txt,color):
    for _ in track(range(100), description=f'[{color}]{txt}'):
        time.sleep(0.01)

def probability(um, rw, schat=False, req=[]):
    count = 0
    hw = True
    for w in um:
        if w in rw:
            count += 1
    per = float(count) / float(len(rw))
    for w in req:
        if w not in um:
            hw = False
            break
    if hw or schat:
        return int(per * 100)
    else:
        return 0



def menu():
    os.system("clear")
    print(Fore.YELLOW+"""
              
            -_________________-_________________-
            |                                   |
            |  |-_-| Welcome to E0 Bot!  |-_-|  |
            -_________________-_________________-
            
    """)
    
    print("[1] Face Dedection")
    print("[2] Object Dedection")
    print("")
    n = input(Fore.RED+"Please select : ")
    if n=="1":
        os.system("python3 EFace.py")



def help():
    os.system("clear")
    print(Fore.YELLOW+"""
              
            -_________________-_________________-
            |                                   |
            |  |-_-| Welcome to E0 Bot!  |-_-|  |
            -_________________-_________________- 
            
    """)
    print(Fore.YELLOW+"help  : To List Commands")
    print(Fore.YELLOW+"menu  : To Print Menu (Other Functions Of Bot)")
    print(Fore.YELLOW+"clear : To Clear Chat")
    print(Fore.YELLOW+"exit  : To Exit")
    print(Fore.YELLOW+"dir   : To Dir Files")
    print(Fore.YELLOW+"ls    : To List Files In Directory")
    print(Fore.YELLOW+"face  : To Run Face Dedection")





def check_all_messages(message):
    high = {}
    def dns(bchat, lw, schat=False, req=[]):
        nonlocal high
        high[bchat] = probability(message, lw, schat, req)

    dns('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo','hola','salam','merhaba'], schat=True)
    dns('See you!', ['bye', 'goodbye'], schat=True)
    dns('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], req=['how'])
    dns('You\'re welcome!', ['thank', 'thanks'], schat=True)
    dns('Thank you!', ['i', 'love', 'code', 'palace'], req=['code', 'palace'])
    dns('Sure!',['want', 'to', 'be', 'my','friend'],schat=True)
    dns('My name is E0. And I created by Err0r. Err0r is python,cpp and ruby developer and competitive programmer.',['name', 'who', 'who are you', 'who are you', 'who are you?','are you?','are you'],schat=True)
    dns('I know python,c and java script languages.',['want', 'ruby', 'cpp', 'python','which language','do you know ?','know?','know','programming language'],schat=True)
    dns('',["play?","game?",'what we can do?','what we can do','what we can','what we can?','what can you do?','what can you do','what can you?',"what can you"],schat=True)
    dns('Yess...',['are you okey?','you okey?','you ok?','you okey'],schat=True)
    dns('I am feeling bad.','I am sad. Hope you are better.',['feel?','how are you feel?','feelings?'],req='feel')
    
    dns('WOW', ['wow', 'awsome', 'good', 'cool'], schat=True)
    dns(E0.R_ADVICE, ['give', 'advice'], req=['advice'])
    dns(E0.R_EATING, ['what', 'you', 'eat'], req=['you', 'eat'])
    dns(E0.R_GAME, ['what', 'game', 'you','play'], req=['game', 'play'])
    
    dns("""Elon Musk, aka Elon Reeve Musk, is an engineer, industrial designer, tech entrepreneur, 
and philanthropist. Apart from his birthplace of South Africa, he is a Canadian and US citizen 
and lives in the USA, where he immigrated at the age of 20.
    """,['elon musk','musk','elon'],schat=True)
    
    dns("""William Henry Bill Gates III or better known as Bill Gates, American entrepreneur,
software developer, author, investor and businessman
    """,['bill gates','bill','gates'],schat=True)

    dns("""Jeffrey Preston Bezos is an American internet entrepreneur, industrialist, media owner, and investor,
best known as the founder, CEO, and chairman of the worldwide technology company Amazon. Before 2017, 
Bezos, who was one of the first hundred billionaires on the Forbes wealth index list, became the richest 
man in the world after 2017.
    """,['jeff','bezos','jeff bezos'],schat=True)

    bestm = max(high, key=high.get)

    return E0.unknown() if high[bestm] < 1 else bestm

def chat(user_input):
    sm = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    dns = check_all_messages(sm)
    return dns

def chatbot():
    os.system('clear')
    print(Fore.YELLOW+"""
              
            -_________________-_________________-
            |                                   |
            |  |-_-| Welcome to E0 Bot!  |-_-|  | 
            -_________________-_________________- 
            
    """)
    
    loading("Loading...","yellow")
    while True:
        x = input(Fore.RED+'You : ')
        print(Fore.YELLOW+'Bot : ' + chat(x) )
        if(x == "exit" or x == "quit" or x == 'break'):
            print(Fore.BLACK+"Exitting...")
            time.sleep(2)
            break
        if(x == "list" or x == "help"):
            help()
        if(x == "ls" or x == "LS"):
            os.system('ls')
        if(x == "FACE" or x == "face"):
            os.system('python3 EFace.py')
        if(x == "dir" or x == "DIR"):
            os.system("dir")
        if(x == "menu"):
            menu()
        elif(x == "clear"):
            chatbot()
chatbot()
