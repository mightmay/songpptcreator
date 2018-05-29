

from flask import Flask



app = Flask(__name__)
returnstring = ''
@app.route('/')
def hello_world():
    returnstring="test"
    return(returnstring)

if __name__ == '__main__':
    app.run()
