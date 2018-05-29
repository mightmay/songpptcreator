

from flask import Flask
import sys, traceback


app = Flask(__name__)
returnstring = ''
@app.route('/')
def hello_world():
    returnstring="start..."
    returnstring=returnstring+"import..."
    import createppt
    returnstring=returnstring+"createppt.imported..."

    try:
        import lxml
    except Exception as e:
        tb = e.__traceback__
        tb = traceback.format_exc()
        returnstring=returnstring+ tb
        return (returnstring)
    return(returnstring)

if __name__ == '__main__':
    app.run()
