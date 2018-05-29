from flask import Flask
import sys
import traceback
import os

sys.path.append("D:\\home\\site\\wwwroot\\pylib")
import xml.dom.minidom
from xml.dom.minidom import parse
from xml.dom import minidom
import xml.dom.minidom
app = Flask(__name__)
#import createppt



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


    return(returnstring)

if __name__ == '__main__':
    app.run(debug=True)
