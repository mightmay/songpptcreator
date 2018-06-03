import os
import sys
import traceback
import os 

from pptx.dml.color import RGBColor

from flask import Flask, request, send_from_directory, send_file 
import xml.dom.minidom
from xml.dom.minidom import parse
from xml.dom import minidom
import xml.dom.minidom


#test value
searchname="พระคุณพระเจ้า"
    
def getsongxmlfilename(searchname):

    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    

    songdirectory = os.path.join(APP_ROOT, 'songdata')
    directoryfile = os.path.join(songdirectory, 'songdirectory.xml')
    directoryfile2 = os.path.join(songdirectory, 'songdirectory.xml')
    # Open XML document containing song directory using minidom parser
    songdirectory = minidom.parse(directoryfile)

    songsname = songdirectory.getElementsByTagName("song")
    for song in songsname:
        if song.getAttribute('name') == searchname:
  
            xmlfilename=song.firstChild.data
            xmlfilename= str(xmlfilename)
            APP_ROOT = os.path.dirname(os.path.abspath(__file__))
            songdirectory2 = os.path.join(APP_ROOT, 'songdata')
            pathtoxmlfile = os.path.join(songdirectory2, xmlfilename)
            print(pathtoxmlfile)
            return(pathtoxmlfile)
    print("song not found in directory")
    return(-1)
    
def getrgbcolorcode(colorname):
    my_red=RGBColor(244, 66, 66)
    my_orange=RGBColor(0xFF, 0x7F, 0x50)
    my_black=RGBColor(0, 0, 0)
    my_blue=RGBColor(58, 112, 188)
    my_green=RGBColor(47, 191, 57)
    my_yellow=RGBColor(255, 251, 71)
    my_purple=RGBColor(163, 31, 193)
    my_white=RGBColor(255, 255, 255)

    colorcode = {
		"red" : my_red,
		"black" : my_black,
        "blue" : my_blue,
		"green" : my_green,
		"yellow" : my_yellow,
		"purple" : my_purple,
		"orange" : my_orange,
        "white" : my_white
	}
    
    returncolor=(colorcode[colorname])
    return(returncolor)

