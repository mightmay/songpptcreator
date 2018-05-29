from flask import Flask, request, send_from_directory, send_file 
import sys
import traceback
import os

sys.path.append("D:\\home\\site\\wwwroot\\pylib")
import xml.dom.minidom
from xml.dom.minidom import parse
from xml.dom import minidom
import xml.dom.minidom
app = Flask(__name__)
from createppt import *

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 
lyricfile = os.path.join(APP_ROOT, 'songdata/amazing grace.xml')
savedirectory = os.path.join(APP_ROOT, 'finishedppt')
savefile = os.path.join(savedirectory, 'WorshipSongs.pptx')

songname= lyricfile

thai=1
english=1
chord=1


@app.route('/')
def hello_world():
    returnstring="start..."
    returnstring=returnstring+"import..."
    try:
        from lxml import etree
        import pptx
    except Exception:
        tb=str(traceback.format_exc())
        return(tb)

    returnstring=returnstring+"imported..."

    APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 
    lyricfile = os.path.join(APP_ROOT, 'songdata/amazing grace.xml')
    createppt.getsongdata(lyricfile,1,1,1)
    try:
        return send_file(savefile,as_attachment=True)
    except Exception as e:
        return str(e)
    
    return str(sys.path)

    return(returnstring)

if __name__ == '__main__':
    app.run(debug=True)
