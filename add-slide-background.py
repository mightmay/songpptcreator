# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 05:33:26 2019

@author: LERTSIRIKARN
"""
from zipfile import ZipFile
import os
import xml.etree.ElementTree as ET
from shutil import copyfile

def extractzipfile(filepath):
    
    print('Extract all files in pptx to different directory')
    # Create a ZipFile Object and load sample.zip in it
    with ZipFile(filepath, 'r') as zipObj:
       # Extract all the contents of zip file in different directory
       zipObj.extractall('temp-folder/unpacked-pptx')
       
def editxml(xmlfilefolderpath,slidenumber):
       slidenumberasstring = str(slidenumber)
       xmlfilepath =xmlfilefolderpath+"/"+"slide" +slidenumberasstring+".xml"
       with open(xmlfilepath, 'r') as file:
           data = file.read().replace('\n', '')
       index = data.find('<p:spTree>')
       background_data_as_string = r"""<p:bg><p:bgPr><a:blipFill dpi="0" rotWithShape="1"><a:blip r:embed="rId2"><a:lum/></a:blip><a:srcRect/><a:stretch><a:fillRect l="-17000" r="-17000"/></a:stretch></a:blipFill><a:effectLst/></p:bgPr></p:bg>"""
       print(data[:index])
       output_data = data[:index] + background_data_as_string + data[index:]
       writefile = open(xmlfilepath,"w") 
       writefile.write(output_data)
       writefile.close()

def addbackgroundimagefiletomediafolder(imagefilepath):
    
    directory = 'temp-folder/unpacked-pptx/ppt/media'
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    fileout=directory+"/image1.jpg"
    
    copyfile(imagefilepath, fileout)
    print(fileout)
   
    
def main():

    filepath = 'temp-folder/WorshipSongs.pptx'
    
    extractzipfile(filepath)
    xmlfilefolderpath = 'temp-folder/unpacked-pptx/ppt/slides'
    editxml(xmlfilefolderpath,1)
    imagefilepath='images/1001.jpg'
    addbackgroundimagefiletomediafolder(imagefilepath)
if __name__ == '__main__':
   main()