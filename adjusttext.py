import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE

from flask import Flask, request, send_from_directory, send_file 
import xml.dom.minidom
from xml.dom.minidom import parse
from xml.dom import minidom
import xml.dom.minidom

def autoaddnewline(inputstring,fontsize,langcount,language):
    slist = list(inputstring)
    totalchar=len(inputstring)
    charcounter=0
    addedline=False
    for cidx, char in enumerate(slist):
       charcounter=charcounter+1
       
       if( (charcounter>(totalchar/(8/langcount))) and char==' ' and language=='thai'):
           slist[cidx]='\n'
           charcounter=0
           addedline=True
           
       if( (charcounter>((totalchar-4)/(8/langcount))) and (char=='.' or char==',' or char==';') and (language=='english' or language=='mienthai')):
           slist[cidx]='\n'
           charcounter=0
           addedline=True
           
       if(charcounter>95-fontsize):
           return (-1)
       if(charcounter>85-fontsize and language=='english'):
           return (-1)
           
    returnstr= "".join(slist)
    print(returnstr)
    if(addedline==False):
        return (-1)
    return returnstr

#inputstring='พระคุณพระเจ้านั้นแสนชื่นใจ ช่วยได้คนชั่วอย่างฉัน ครั้งนั้นฉันหลงพระองค์ตามหา ตาบอดแต่ฉันเห็นแล้ว'

#autoaddnewline(inputstring,35,1,'thai')