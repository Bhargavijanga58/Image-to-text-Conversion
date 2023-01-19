##importing required packages
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
try:
from PIL import Image
except ImportError:
import Image
import pytesseract,re
from pytesseract import *
img2=cv2.imread("ss12.png")#df4
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
custom_config = r'--oem 3 --psm 6' pytesseract.image_to_string(gray, config=custom_config)
string=pytesseract.image_to_string(gray)

#Drawing boxes around recognised text using image_to_data() method:
details = pytesseract.image_to_data(gray, output_type=Output.DICT, config=custom_config, lang='eng')
total_boxes = len(details['text'])
for sequence_number in range(total_boxes):
if int(details['conf'][sequence_number]) >30:
(x, y, w, h) = (details['left'][sequence_number], details['top'][sequence_number], details['width'][sequence_number], details['height'][sequence_number])
threshold_img = cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)

t=string.split('\n')
#FOR SWIGGY details:
def ID_rest(t):
for i in t:
if i!='':
if re.findall(r'\d+ [A-z]+',i):
OR=i.split()[0]
RS=" ".join(i.split()[1:])
return OR,RS

iD,RS=ID_rest(t)
items=[]
for i in t:
if i!='':
if re.findall(r'[A-Za-z0-9 +]*[A-Za-z0-9 +][A-Za-z0-9 +]* \d$',i):
items.append(i)

items=",".join(items)
total=re.findall(r'\d+',string)
total=total[-1]

#FOR AADHAR details:
sg=strg.split('\n')
for j in sg:
if j!='':
if re.findall(r'^\d{4}\s\d{4}\s\d{4}$',j):
x=j

for j in sg:
if j!='':
if re.findall(r'([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$',j):
y=j.split()[-1]
if re.findall(r'([0-2][0-9]|(3)[0-1])(\-)(((0)[0-9])|((1)[0-2]))(\-)\d{4}$',j):
y="".join(j.split()[-1])

for j in sg:
if j!='':
if re.findall(r'Female|Male',j):
for q in j.split():
if q=='Male' or q=="Female":
gender =q
for j in sg:
if j!='':
if re.findall(r'/ Name',j):
p=sg.index(j)
n=sg[p+1]
