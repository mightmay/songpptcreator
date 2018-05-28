# -*- coding: utf-8 -*-
"""
Created on Sat May 26 20:47:23 2018

@author: Computer
"""

import os
from . import createppt
from flask import Flask, request, send_from_directory, send_file 

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 

savedirectory = os.path.join(APP_ROOT, 'finishedppt')
savefile = os.path.join(savedirectory, 'WorshipSongs.pptx')

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 
        lyricfile = os.path.join(APP_ROOT, 'songdata/amazing grace.xml')
        createppt.getsongdata(lyricfile,1,1,1)
        try:
            return send_file(savefile,as_attachment=True)
        except Exception as e:
            return str(e)
    


    return app