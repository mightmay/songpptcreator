from flask import Flask, request, send_from_directory, send_file ,render_template, request
import sys
import traceback
import os

sys.path.append("D:\\home\\site\\wwwroot\\pylib")
import xml.dom.minidom
from xml.dom.minidom import parse
from xml.dom import minidom
import xml.dom.minidom
app = Flask(__name__)
from createppt import getsongdata
from getinfo import getsongxmlfilename,getrgbcolorcode
from pptx import Presentation


APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 
lyricfile = os.path.join(APP_ROOT, 'songdata/amazing grace.xml')
savedirectory = os.path.join(APP_ROOT, 'finishedppt')
savefile = os.path.join(savedirectory, 'WorshipSongs.pptx')

songname= lyricfile

thai=1
english=1
chord=1
first_language="thai"
second_language="english"
third_language="mienthai"

first_color="thai"
second_color="english"
third_color="mienthai"


@app.route('/')
def student():
   return render_template('mainpage.html')

@app.route('/createpptx',methods = ['POST', 'GET'])
def createpptxfile():

    try:
        from lxml import etree
        import pptx
    except Exception:
        tb=str(traceback.format_exc())
        return(tb)

    
    if request.method == 'POST':
        songlistinput = request.form['songlist']
        first_language = request.form['chooselanguage1']
        second_language = request.form['chooselanguage2']
        third_language = request.form['chooselanguage3']
        firsttextsizeint = request.form['textsize1']
        secondtextsizeint = request.form['textsize2']
        thirdtextsizeint = request.form['textsize3']
        firsttextcolor = request.form['choosecolor1']
        secondtextcolor = request.form['choosecolor2']
        thirdtextcolor = request.form['choosecolor3']

    else:
        songlistinput = request.args.get('songlist')
        firsttextsizeint = request.args.get['textsize1']
        secondtextsizeint = request.args.get['textsize2']
        thirdtextsizeint = request.args.get['textsize3']
        first_language = request.args.get['chooselanguage1']
        second_language = request.args.get['chooselanguage2']
        third_language = request.args.get['chooselanguage3']
        firsttextcolor = request.args.get['choosecolor1']
        secondtextcolor = request.args.get['choosecolor2']
        thirdtextcolor = request.args.get['choosecolor3']



    firsttextcolorrgb= getrgbcolorcode(firsttextcolor)
    secondttextcolorrgb= getrgbcolorcode(secondtextcolor)
    thirdtextcolorrgb= getrgbcolorcode(thirdtextcolor)

    songlist=songlistinput.split(",")
    # create presentation
    prs = Presentation()
    
    songlist
    
    # get song xml file path for each song then put it in a list
    filepathlist=[]
    for song_itr in songlist:
        song_itr_cleaned = song_itr.replace(" ", "")
        filepathlist.append(getsongxmlfilename(song_itr_cleaned))
    
    print(filepathlist)

    # create the pptx file
    for fp_itr in filepathlist:
        if fp_itr == -1:
            return("song not found")
        getsongdata(prs,fp_itr,first_language,second_language,third_language,firsttextsizeint,secondtextsizeint,thirdtextsizeint,firsttextcolorrgb,secondttextcolorrgb,thirdtextcolorrgb,0)
        
    prs.save(savefile)
    try:
        return send_file(savefile,as_attachment=True)
    except Exception as e:
        return str(e)

    return(returnstring)

if __name__ == '__main__':
    app.run(debug=True)
