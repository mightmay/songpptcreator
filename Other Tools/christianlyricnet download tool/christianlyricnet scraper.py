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
#print(data.head())
startchorus=[]
startverse=[]
nonstart=[]
linkslist=data.URL
cantgenlist=[]
songdirectory=ET.Element('all')

for itr in range(len(linkslist)):
    failed=0
    page = requests.get(linkslist[itr])
    #print(page.text)
    tree = html.fromstring(page.content)
 #   print("tree:",tree)
    songtitle = tree.xpath('//*[@id="col-lyrics"]/h1/text()')
    try:
        songtitle=songtitle[0].replace('lyrics', '')
        print(itr,'song title extracted: ',songtitle)
    except:
        failed=1
        continue
    #songtitle=songtitle.replace(" ", "")
    
    #print(songtitle)
    try:
        songcontent = tree.xpath('//*[@id="lyrics"]/text()')
        seperator = ''
        songcontent=seperator.join(songcontent)
    except:
        failed=1
        continue
   # print('songcontent raw:',songcontent)

    versesarray=songcontent.split("\r\n\r\n")
#    print(versesarray)
    versecounter=1
    choruscounter=1
    
    # create the file structure
    song = ET.Element('song')  
    item1 = ET.SubElement(song, 'thainame')  
    item0 = ET.SubElement(song, 'englishname')  
    item2 = ET.SubElement(song, 'mienthainame')
    item3 = ET.SubElement(song, 'order')  
    englishverses = ET.SubElement(song, 'english')  
     
    item0.text = songtitle
    item1.text = 'none'
    item2.text = 'none'
    segmentcounter=1

    versearray=[]
    orderarray =[]

    for vitr in versesarray:
        segmentcount="segment"+str(segmentcounter)
        orderarray.append(segmentcount)
        versetext=vitr.replace("\r\n",". ")
        versetext=versetext.replace("\n","")
        versetext=versetext.replace(" . ",". ")
        versetext=versetext.replace(":.",":")        
        versetext=versetext.replace("..",".")
        versetext=versetext.replace(",.",",")
        versetext=versetext.replace(",.",",")
        versetext=versetext.replace("&#146;","'")
       
        ET.SubElement(englishverses, segmentcount).text=versetext
        segmentcounter=segmentcounter+1

    temporderstr=''
    for oitr in range(len(orderarray)):
        temporderstr=temporderstr+orderarray[oitr]
        if(oitr!=len(orderarray)-1):
            temporderstr=temporderstr+','
    item3.text=temporderstr 


    # create a new XML file with the results
    if failed==0:
        namefordirectory = songtitle.lower()
        namefordirectory = namefordirectory.replace(' ','')
        namefordirectory = namefordirectory.replace(',','')
        namefordirectory = namefordirectory.replace("*",'')
        namefordirectory = namefordirectory.replace("'",'')
        namefordirectory = namefordirectory.replace("/",'')
        namefordirectory = namefordirectory.replace("\\",'')
        namefordirectory = namefordirectory.replace("\t",'')
        namefordirectory = namefordirectory.replace('?','')
        namefordirectory = namefordirectory.replace(")",'')
        namefordirectory = namefordirectory.replace("(",'')
        namefordirectory = namefordirectory.replace("-",'')
        namefordirectory = namefordirectory.replace("[",'')
        namefordirectory = namefordirectory.replace("]",'')
        namefordirectory = namefordirectory.replace('"','')
        namefordirectory = namefordirectory.replace('!','')
        namefordirectory = namefordirectory.replace(':','')
        namefordirectory = namefordirectory.replace('.','')
        mydata = prettify(song)  
        myfile = open(namefordirectory+".xml", "w",encoding="utf-8")
    #    print(mydata)
        myfile.write(mydata)
        myfile.close()

        ET.SubElement(songdirectory,'song',name=namefordirectory).text=namefordirectory+'.xml'
        
    mydata2 = prettify(songdirectory)  
    myfile2 = open("songdirectory.xml", "w",encoding="utf-8")
    #print(mydata2)
    myfile2.write(mydata2)
    myfile2.close()

    cantgendf = pd.DataFrame(cantgenlist, columns=["colummn"])
    cantgendf.to_csv('cantgenlist.csv', index=False)
        


