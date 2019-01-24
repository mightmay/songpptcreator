import pandas as pd
from lxml import html
import requests
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree, tostring

from xml.etree import ElementTree
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'unicode')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

class MySubElement:
  def __init__(parent, name):
        self=ET.SubElement(parent, name)

import re
data = pd.read_csv("alllinks.csv")
print(data.head())

linkslist=data.URL
cantgenlist=[]
thaicharlist=['ก' , 'ข' , 'ฃ' , 'ค' , 'ฅ' , 'ฆ', 'ง' , 'จ' , 'ฉ' , 'ช' , 'ซ' , 'ฌ' , 'ญ' , 'ฎ', 'ฏ' , 'ฐ' , 'ฑ' , 'ฒ' , 'ณ' , 'ด' , 'ต' , 'ถ', 'ท' , 'ธ' , 'น' , 'บ' , 'ป' , 'ผ' , 'ฝ' , 'พ', 'ฟ' , 'ภ' , 'ม' , 'ย' , 'ร' , 'ล' , 'ว' , 'ศ', 'ษ' , 'ส' , 'ห' , 'ฬ' , 'อ' , 'ฮ']
songdirectory=ET.Element('all')
for itr in range(len(linkslist)):
    page = requests.get(linkslist[itr])
    tree = html.fromstring(page.content)
    #print(tree)
    songtitle = tree.xpath('//title/text()')
    songtitle=songtitle[0]
    songtitle=songtitle.replace(" ", "")
    songtitle=songtitle.replace("\\", "")
    songtitle=songtitle.replace("/", "")
    
    #print(songtitle)
    songcontent = tree.xpath('//span[@id="spanLyric"]/text()')
    print(songcontent)

    versecounter=1
    choruscounter=1
    
    # create the file structure
    song = ET.Element('song')  
    item0 = ET.SubElement(song, 'thainame')  
    item1 = ET.SubElement(song, 'englishname')  
    item2 = ET.SubElement(song, 'mienthainame')
    item3 = ET.SubElement(song, 'order')  
    thaiverses = ET.SubElement(song, 'thai')  
     
    item0.text = songtitle
    item1.text = 'none'
    item2.text = 'none'
    versecounter=1
    choruscounter=1
    versearray=[]
    orderarray =[]
    failed=0
    if "รายชื่อเพลงนมัสการที่มีข้อความ" in songtitle:
        failed=1
        
    for contentline in songcontent:

        containTH=0
        for charitr in thaicharlist:
            if charitr in contentline: containTH=1
            
        if  containTH==1:
            print(",")
            print(contentline)
            print(",")
            containVerseNum=0
            numlist = ["1" , "2" , "3" , "4" , "5" , "6", u'\xa0\xa0\xa0\xa0']
            for numlistitr in numlist:
               if numlistitr in contentline[0:15]: containVerseNum=1
            try:
               if containVerseNum==1:
                   contentline=contentline.replace(u'\xa0', u'')
                   contentline=contentline.replace("\r\n"," ")
                   contentline=contentline.replace('\n',' ')
                   contentline=contentline.replace('\t',' ')

                   while '  ' in contentline:
                        contentline = contentline.replace('  ', ' ')
                   versearray.append(contentline)
                   print("v found",contentline)
                   orderarray.append("verse"+str(versecounter))
                   versecounter=versecounter+1
               elif ( '*' or 'CHORUS' or 'chorus' or 'ร้องรับ' or'Chorus') in contentline[0:10]:
                   contentline=contentline.replace(u'\xa0', u'')
                   contentline=contentline.replace("\r\n"," ")
                   contentline=contentline.replace('\n',' ')
                   contentline=contentline.replace('\t',' ')
              
                   while '  ' in contentline:
                        contentline = contentline.replace('  ', ' ')
                   versearray.append(contentline)
                   print("Chorus found",contentline)
                   orderarray.append("chorus"+str(choruscounter))
                   choruscounter=choruscounter+1
               else:
                   index=len(versearray)-1
                   contentline=contentline.replace(u'\xa0', u'')
                   contentline=contentline.replace("\r\n"," ")
                   contentline=contentline.replace('\n',' ')
                   contentline=contentline.replace('\t',' ')

                   while '  ' in contentline:
                        contentline = contentline.replace('  ', ' ')
                   versearray[index]=versearray[index]+contentline
                   
            except:
               print("can't gen verse")
               failed=1
               cantgenlist.append(linkslist[itr])
    print(versearray)
    print(orderarray)
    for itrr in range(len(versearray)):
        ET.SubElement(thaiverses, orderarray[itrr]).text= versearray[itrr].strip()

    temporderstr=''
    for oitr in range(len(orderarray)):
        temporderstr=temporderstr+orderarray[oitr]
        if(oitr!=len(orderarray)-1):
            temporderstr=temporderstr+','
    item3.text=temporderstr    
    # create a new XML file with the results
    if failed==0:
        
        mydata = prettify(song)  
        myfile = open(songtitle+".xml", "w",encoding="utf-8")
        print(mydata)
        myfile.write(mydata)
        myfile.close()
        ET.SubElement(songdirectory,'song',name=songtitle).text=songtitle+'.xml'
        
    mydata2 = prettify(songdirectory)  
    myfile2 = open("songdirectory.xml", "w",encoding="utf-8")
    print(mydata2)
    myfile2.write(mydata2)
    myfile2.close()

    cantgendf = pd.DataFrame(cantgenlist, columns=["colummn"])
    cantgendf.to_csv('cantgenlist.csv', index=False)
        


