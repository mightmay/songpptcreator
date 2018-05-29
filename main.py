import os
import sys
sys.path.append("D:\\home\\site\\wwwroot\\pylib")
import traceback
import os 
try:
    import createppt
except Exception as e:
    tb = e.__traceback__
    tb = traceback.format_exc()
    return tb

from flask import Flask, request, send_from_directory, send_file 

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 

savedirectory = os.path.join(APP_ROOT, 'finishedppt')
savefile = os.path.join(savedirectory, 'WorshipSongs.pptx')

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        import lxml
    except Exception as e:
        tb = e.__traceback__
        tb = traceback.format_exc()
        return tb
    try:
        from pptx import Presentation
    except Exception as e:
        tb = e.__traceback__
        tb = traceback.format_exc()
        return tb
    
    APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 
    lyricfile = os.path.join(APP_ROOT, 'songdata/amazing grace.xml')
    createppt.getsongdata(lyricfile,1,1,1)
    try:
        return send_file(savefile,as_attachment=True)
    except Exception as e:
        return str(e)
    
    return str(sys.path)

if __name__ == '__main__':
  app.run()
