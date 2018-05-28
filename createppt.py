# -*- coding: utf-8 -*-
"""
Created on Sun May 27 00:00:04 2018

@author: Computer
"""
import os
from pptx import Presentation
from flask import Flask, request, send_from_directory, send_file 

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 
lyricfile = os.path.join(APP_ROOT, 'songdata/amazing grace.xml')
savedirectory = os.path.join(APP_ROOT, 'finishedppt')
savefile = os.path.join(savedirectory, 'WorshipSongs.pptx')

songname= lyricfile

thai=1
english=1
chord=1

import os
from xml.dom.minidom import parse
from xml.dom import minidom
import xml.dom.minidom

def getsongdata(songname,thai,english,chord):
    
    # create presentation
    prs = Presentation()
    bullet_slide_layout = prs.slide_layouts[1]
    
    slide = prs.slides.add_slide(bullet_slide_layout)
    shapes = slide.shapes
    
    title_shape = shapes.title
    body_shape = shapes.placeholders[1]
    
    title_shape.text = 'Adding a Bullet Slide'
    
    tf = body_shape.text_frame
    tf.text = 'Find the bullet slide layout'
    
    p = tf.add_paragraph()
    p.text = 'Use _TextFrame.text for first bullet'
    p.level = 1
    
    p = tf.add_paragraph()
    p.text = 'Use _TextFrame.add_paragraph() for subsequent bullets'
    p.level = 2
    
    prs.save(savefile)
    
    # Open XML document containing song data using minidom parser
    songdata = minidom.parse(songname)
    
    # get song ordering
    order = songdata.getElementsByTagName("order")[0]
    order_list=(order.childNodes[0].data)
    order_list = order_list.split(",")
    print(order_list)
    
    
    for versenum in order_list:
        vnum=str(versenum)


        if thai == 1:
            thaidata=songdata.getElementsByTagName("thai")
            for th in thaidata:
                print(thaidata)
                print(vnum)
                thailyric=th.getElementsByTagName(vnum)[0]
                thailyric=(thailyric.childNodes[0].data)
                print(thailyric)
                
def download_file():
    return send_from_directory(savedirectory,savefile, as_attachment=True)                

            
        
getsongdata(songname,thai,english,chord)
