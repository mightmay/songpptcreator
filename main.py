

from flask import Flask
returnstring="start..."
returnstring=returnstring+"import..."


app = Flask(__name__)
returnstring = ''
@app.route('/')
def hello_world():

    return(returnstring)

if __name__ == '__main__':
    app.run()
