from flask import Flask
import sys
import traceback
app = Flask(__name__)
#import createppt

#    try:
#        import lxml
#    except Exception:
#        tb=str(traceback.format_exc())
#        return(tb)
@app.route('/')
def hello_world():
    returnstring="start..."
    returnstring=returnstring+"import..."
    returnstring=returnstring+"createppt.imported..."


    return(returnstring)

if __name__ == '__main__':
    app.run()
