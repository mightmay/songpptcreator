import os
from . import createppt


from flask import Flask, request, send_from_directory, send_file 

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 

savedirectory = os.path.join(APP_ROOT, 'finishedppt')
savefile = os.path.join(savedirectory, 'WorshipSongs.pptx')

@app.route('/')
def hello_world():
    APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 
    lyricfile = os.path.join(APP_ROOT, 'songdata/amazing grace.xml')
    #createppt.getsongdata(lyricfile,1,1,1)
    try:
        return "test"
    except Exception as e:
        return str(e)
    

if __name__ == '__main__':
  app.run()
