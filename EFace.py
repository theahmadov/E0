import numpy as np
import cv2 
import re
import os
import sys
import logging
import time
from colorama import Fore,Back,Style
from bs4 import BeautifulSoup

class bcolors:
    OK = '\033[92m' 
    WA = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m'

os.system("clear")
logging.basicConfig(level=logging.DEBUG, filename="log.txt", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  
cap = cv2.VideoCapture(0)
  
while True: 
  
    ret, img = cap.read() 
  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
        print(Fore.BLACK+"[+] Face Dedected. Waiting Command... ")
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        logging.info(Fore.GREEN+"[+] Face Dedected. Waiting Command... ")
        time.sleep(0.01)
  

        cv2.imshow('img',img)
  
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        print(Fore.RED+"[-] Quitting...")
        logging.info("[-] Quitting...")
        break
    elif k == 32:
        print(Fore.RED+"[-] Target Destroying...")
        logging.info("[-] Target Destroying...")
        time.sleep(2)
        print(Fore.GREEN+"[+] Target Destroyed...")
        logging.info("[+] Target Destroyed...")
        print(Fore.RED+"[+] Image Saving...")
        logging.info(Fore.GREEN+"[+] Image Saved Succesfully... (log.txt)")
        filename = 'log.jpg'
        cv2.imwrite(filename, img)
        break

cap.release()
cv2.destroyAllWindows()
