import os
import sys
sys.path.append("D:\\home\\site\\wwwroot\\pymodules")
sys.path.append("D:\\home\\site\\wwwroot\\pylib")
import traceback
import os 
os.environ['PYTHON_EGG_CACHE'] = '/usr/local/pylons/python-eggs' 

#from .createppt import * 
from flask import Flask, request, send_from_directory, send_file 

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 

savedirectory = os.path.join(APP_ROOT, 'finishedppt')
savefile = os.path.join(savedirectory, 'WorshipSongs.pptx')

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        from pptx import Presentation
    except Exception as e:
        tb = e.__traceback__
        tb = traceback.format_exc()
        return tb
    return str(sys.path)

if __name__ == '__main__':
  app.run()
