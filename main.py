returnstring = 'importing<br>'
from flask import Flask

returnstring = returnstring + 'import done<br>'

app = Flask(__name__)
returnstring = ''
@app.route('/')
def hello_world():
  return(returnstring)

if __name__ == '__main__':
  app.run()
