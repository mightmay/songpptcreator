from flask import Flask
import sys
import traceback
app = Flask(__name__)
returnstring="start..."
@app.route('/')
def hello_world():

    returnstring=returnstring+"import..."
#    from createppt import
    returnstring=returnstring+"createppt.imported..."
#    try:
#        import lxml
#    except Exception:
#        tb=str(traceback.format_exc())
#        return(tb)

    return(returnstring)

if __name__ == '__main__':
    app.run()
