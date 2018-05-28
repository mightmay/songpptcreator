import os
#from . import createppt
from flask import Flask, request, send_from_directory, send_file 
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

if __name__ == '__main__':
  app.run()