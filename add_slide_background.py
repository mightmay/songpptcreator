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
       
def editxml(xmlfilefolderpath,slidenumber,imagename):

       slidenumberasstring = str(slidenumber)
       
       # edit xml to add background in slide1.xml
       xmlfilepath =xmlfilefolderpath+"/"+"slide" +slidenumberasstring+".xml"
       print(xmlfilepath)
       with open(xmlfilepath, 'r',encoding='utf-8') as file:
           data = file.read().replace('\n', '')
       index = data.find('<p:spTree>')
       background_data_as_string = r"""<p:bg><p:bgPr><a:blipFill dpi="0" rotWithShape="1"><a:blip r:embed="rId2"><a:lum/></a:blip><a:srcRect/><a:stretch><a:fillRect l="-17000" r="-17000"/></a:stretch></a:blipFill><a:effectLst/></p:bgPr></p:bg>"""
      # print(data[:index])
       output_data = data[:index] + background_data_as_string + data[index:]
       writefile = open(xmlfilepath,"w",encoding='utf-8') 
       writefile.write(output_data)
       writefile.close()
       
       #edit xml to add background in _rels/slide1.xml.rels
       xmlfilepath =xmlfilefolderpath+"/_rels/"+"slide" +slidenumberasstring+".xml.rels"
       with open(xmlfilepath, 'r',encoding='utf-8') as file:
           data = file.read().replace('\n', '')
       index = data.find('</Relationships>')
       background_data_as_string_1 = r"""<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/"""
       background_data_as_string_2 = r""""/>"""
       background_data_as_string=background_data_as_string_1+imagename+background_data_as_string_2
       # print(data[:index])
       output_data = data[:index] + background_data_as_string + data[index:]
       writefile = open(xmlfilepath,"w",encoding='utf-8') 
       writefile.write(output_data)
       writefile.close()


def addbackgroundimagefiletomediafolder(imagefilepath,mediafileimagename):
    
    directory = 'temp-folder/unpacked-pptx/ppt/media'
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    fileout=directory+"/"+mediafileimagename
    
    copyfile(imagefilepath, fileout)
    #print(fileout)
   
  
def get_all_file_paths(directory): 
  
    # initializing empty file paths list 
    file_paths = [] 
  
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
  
    # returning all file paths 
    return file_paths         
  
    
import zipfile

    
''' 
    zip_file:
        @src: Iterable object containing one or more element
        @dst: filename (path/filename if needed)
        @arcname: Iterable object containing the names we want to give to the elements in the archive (has to correspond to src) 
'''
def zip_files(src, dst, arcname=None):

    zip_ = zipfile.ZipFile(dst, 'w')
   # print(src, dst)
    for i in range(len(src)):
        if arcname is None:
            #print("src name, ",src[i])
            #print("dir name ",os.path.dirname(src[i]))
            write_location = os.path.dirname(src[i])+os.path.basename(src[i])
            write_location=(src[i])
            write_location=write_location.replace("temp-folder/unpacked-pptx\\","")
            write_location= write_location.replace("\\","/")
         
            zip_.write(src[i], write_location, compress_type = zipfile.ZIP_STORED)
        else:
            zip_.write(src[i], arcname[i], compress_type = zipfile.ZIP_STORED)

    zip_.close()
 
    

def zipdir(path, ziph):
    length = len(path)

    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        folder = root[length:] # path without "parent"
        for file in files:
            ziph.write(os.path.join(root, file), os.path.join(folder, file))

            
def add_background_to_slide_main(pptx_file,save_location,**kwarg):
    
    '''
    input dict
    {
    'image_path' : [slide_number]
    }
    example:
        {
        'images/1001.jpg':[1,2]
        ,
        'images/1002.jpg':[3]
        }
    '''



    # path of the pptx file to add background image too
    filepath = pptx_file

    # extract pptx file    
    extractzipfile(filepath)
        
    # iterage through input dict
    counter = 1
    for key, value in kwarg.items(): 
        counter_as_string=str(counter)
        print(key, ":", value) 
        imagefilepath=key
        imagename="image"+counter_as_string+".jpg"
        mediafileimagename = imagename
        addbackgroundimagefiletomediafolder(imagefilepath,mediafileimagename)

        xmlfilefolderpath = 'temp-folder/unpacked-pptx/ppt/slides'

        for slide_i in value:
            print(xmlfilefolderpath,slide_i,imagename)
            editxml(xmlfilefolderpath,slide_i,imagename)
        counter +=1
    
    pptxfilespath = 'temp-folder/unpacked-pptx'
#    file_paths = get_all_file_paths(pptxfilespath) 
    #zip_files(file_paths, save_location, arcname=None)
    
    zipf = zipfile.ZipFile(save_location, 'w', zipfile.ZIP_STORED)
    zipdir(pptxfilespath, zipf)
    zipf.close()
    
    import shutil
    shutil.rmtree(pptxfilespath)
 
#if __name__ == '__main__':

if __name__ == '__add_background_to_slide_main__':
   filepath = 'finishedppt/WorshipSongs.pptx'
   kwarg  = {
		'images/1001.jpg' : [1,2],
         'images/1002.jpg':[3]
	}
   save_location= 'temp-folder/worship-song-slides-added-bground.pptx'
   add_background_to_slide_main(filepath,save_location,**kwarg)
   
   
   
   
   
   
   
   
   
